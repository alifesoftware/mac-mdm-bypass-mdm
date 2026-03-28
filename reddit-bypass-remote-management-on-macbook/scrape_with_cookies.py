import sqlite3, shutil, hashlib, json, time, datetime, requests
from Crypto.Cipher import AES

# ── Decrypt Chromium cookies ──────────────────────────────────────────────────
password = b'peanuts'
salt = b'saltysalt'
key = hashlib.pbkdf2_hmac('sha1', password, salt, 1, dklen=16)

def decrypt_cookie(enc_val):
    if enc_val[:3] == b'v10':
        enc_data = enc_val[3:]
        iv = b' ' * 16
        cipher = AES.new(key, AES.MODE_CBC, IV=iv)
        decrypted = cipher.decrypt(enc_data)
        pad_len = decrypted[-1]
        return decrypted[:-pad_len].decode('utf-8', errors='replace')
    return enc_val.decode('utf-8', errors='replace') if enc_val else ''

cookie_db = '/home/ubuntu/.browser_data_dir/Default/Cookies'
shutil.copy2(cookie_db, '/tmp/cookies_scrape.db')
conn = sqlite3.connect('/tmp/cookies_scrape.db')
cur = conn.cursor()
cur.execute("SELECT name, encrypted_value, host_key FROM cookies WHERE host_key LIKE '%reddit%'")
rows = cur.fetchall()
conn.close()

cookies = {}
for name, enc_val, host in rows:
    cookies[name] = decrypt_cookie(enc_val)

print(f"Decrypted {len(cookies)} Reddit cookies")

# ── Fetch Reddit JSON ─────────────────────────────────────────────────────────
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.reddit.com/",
}

SESSION = requests.Session()
SESSION.headers.update(HEADERS)
SESSION.cookies.update(cookies)

def fetch(url, params=None):
    time.sleep(0.8)
    r = SESSION.get(url, params=params)
    print(f"  GET {url[:80]} -> {r.status_code}")
    if r.status_code == 200:
        return r.json()
    return None

def ts(utc):
    return datetime.datetime.utcfromtimestamp(utc).strftime("%Y-%m-%d %H:%M UTC")

def fetch_more(link_id, children_ids):
    if not children_ids:
        return []
    url = "https://www.reddit.com/api/morechildren.json"
    params = {
        "link_id": link_id,
        "children": ",".join(children_ids[:100]),
        "api_type": "json",
        "limit_children": "false",
        "depth": "10",
    }
    time.sleep(1.0)
    r = SESSION.get(url, params=params)
    print(f"  morechildren -> {r.status_code}")
    if r.status_code == 200:
        return r.json().get("json", {}).get("data", {}).get("things", [])
    return []

def render_comment(comment, depth=0):
    if comment.get("kind") != "t1":
        return ""
    data = comment["data"]
    author = data.get("author", "[deleted]")
    body = data.get("body", "[removed]")
    score = data.get("score", 0)
    created = data.get("created_utc", 0)
    indent = "  " * depth
    lines = [f"{indent}---", f"{indent}**{author}** | Score: {score} | {ts(created)}", ""]
    for line in body.split("\n"):
        lines.append(f"{indent}{line}")
    lines.append("")
    replies = data.get("replies", "")
    if replies and isinstance(replies, dict):
        for child in replies["data"]["children"]:
            if child["kind"] == "t1":
                lines.append(render_comment(child, depth + 1))
            elif child["kind"] == "more":
                more_ids = child["data"].get("children", [])
                if more_ids:
                    lines.append(f"{indent}  *[{len(more_ids)} more replies not loaded]*")
                    lines.append("")
    return "\n".join(lines)

# ── Main ──────────────────────────────────────────────────────────────────────
print("Fetching thread...")
data = fetch(
    "https://www.reddit.com/r/mac/comments/pi9beh/bypass_remote_management_on_macbook_pro_after/.json",
    params={"limit": 500, "depth": 10}
)

if not data:
    print("Failed to fetch thread JSON")
    exit(1)

post_data = data[0]["data"]["children"][0]["data"]
comments_listing = data[1]["data"]["children"]
link_fullname = post_data["name"]

title = post_data.get("title", "")
selftext = post_data.get("selftext", "")
author = post_data.get("author", "[deleted]")
score = post_data.get("score", 0)
num_comments = post_data.get("num_comments", 0)
created = post_data.get("created_utc", 0)
permalink = f"https://www.reddit.com{post_data.get('permalink', '')}"

print(f"Post: {title}")
print(f"Top-level items: {len(comments_listing)}")

# Collect top-level "more" stubs
top_more_ids = []
for child in comments_listing:
    if child.get("kind") == "more":
        top_more_ids.extend(child["data"].get("children", []))

print(f"Top-level more IDs: {len(top_more_ids)}")

# Fetch additional top-level comments
extra_things = []
for i in range(0, len(top_more_ids), 100):
    batch = top_more_ids[i:i+100]
    things = fetch_more(link_fullname, batch)
    extra_things.extend(things)

# Build tree from extra things
def build_tree(things):
    by_name = {}
    roots = []
    for t in things:
        if t["kind"] == "t1":
            t["data"]["_extra_children"] = []
            by_name[t["data"]["name"]] = t
    for t in things:
        if t["kind"] != "t1":
            continue
        pid = t["data"].get("parent_id", "")
        if pid in by_name:
            by_name[pid]["data"]["_extra_children"].append(t)
        else:
            roots.append(t)
    return roots

def render_extra(comment, depth=0):
    if comment.get("kind") != "t1":
        return ""
    data = comment["data"]
    author = data.get("author", "[deleted]")
    body = data.get("body", "[removed]")
    score = data.get("score", 0)
    created = data.get("created_utc", 0)
    indent = "  " * depth
    lines = [f"{indent}---", f"{indent}**{author}** | Score: {score} | {ts(created)}", ""]
    for line in body.split("\n"):
        lines.append(f"{indent}{line}")
    lines.append("")
    for child in data.get("_extra_children", []):
        lines.append(render_extra(child, depth + 1))
    return "\n".join(lines)

# ── Build Markdown ────────────────────────────────────────────────────────────
md = []
md.append(f"# {title}")
md.append("")
md.append(f"**Posted by:** u/{author}  ")
md.append(f"**Subreddit:** r/mac  ")
md.append(f"**Date:** {ts(created)}  ")
md.append(f"**Score:** {score} upvotes | **Comments:** {num_comments}  ")
md.append(f"**Source:** {permalink}")
md.append("")
md.append("---")
md.append("")
md.append("## Original Post")
md.append("")
md.append(selftext)
md.append("")
md.append("---")
md.append("")
md.append("## Comments")
md.append("")
md.append("> *Comments ordered by Reddit's default (top) sort. Indentation reflects nesting depth.*")
md.append("")

count = 0
for child in comments_listing:
    if child["kind"] == "t1":
        md.append(render_comment(child, 0))
        count += 1

extra_roots = build_tree(extra_things)
for root in extra_roots:
    md.append(render_extra(root, 0))
    count += 1

print(f"Total top-level threads rendered: {count}")

output = "\n".join(md)
output = (output
    .replace("&amp;", "&")
    .replace("&gt;", ">")
    .replace("&lt;", "<")
    .replace("&nbsp;", " ")
    .replace("&#39;", "'")
    .replace("&quot;", '"')
    .replace("&#x200B;", "")
)

out_path = "/home/ubuntu/reddit_thread_full_archive.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(output)

print(f"Written to {out_path} ({len(output.splitlines())} lines)")
