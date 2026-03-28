import requests
import json
import time
import datetime

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; RedditScraper/1.0)"}
BASE_URL = "https://www.reddit.com"
POST_ID = "pi9beh"

def fetch_json(url, params=None):
    time.sleep(0.6)  # be polite
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()
    return r.json()

def fetch_more_children(link_id, children_ids):
    """Fetch collapsed/hidden comments via the morechildren API."""
    if not children_ids:
        return []
    url = "https://www.reddit.com/api/morechildren.json"
    params = {
        "link_id": link_id,
        "children": ",".join(children_ids[:100]),  # API limit
        "api_type": "json",
        "limit_children": False,
        "depth": 10,
    }
    time.sleep(0.8)
    r = requests.get(url, headers=HEADERS, params=params)
    r.raise_for_status()
    data = r.json()
    return data.get("json", {}).get("data", {}).get("things", [])

def ts(utc):
    return datetime.datetime.utcfromtimestamp(utc).strftime("%Y-%m-%d %H:%M UTC")

def render_comment(comment, depth=0):
    """Recursively render a comment and its replies as Markdown."""
    if comment.get("kind") != "t1":
        return ""

    data = comment["data"]
    author = data.get("author", "[deleted]")
    body = data.get("body", "[removed]")
    score = data.get("score", 0)
    created = data.get("created_utc", 0)

    indent = "  " * depth
    lines = []
    lines.append(f"{indent}---")
    lines.append(f"{indent}**{author}** | Score: {score} | {ts(created)}")
    lines.append("")
    for line in body.split("\n"):
        lines.append(f"{indent}{line}")
    lines.append("")

    replies = data.get("replies", "")
    if replies and isinstance(replies, dict):
        children = replies.get("data", {}).get("children", [])
        for child in children:
            if child.get("kind") == "t1":
                lines.append(render_comment(child, depth + 1))
            elif child.get("kind") == "more":
                more_ids = child["data"].get("children", [])
                if more_ids:
                    lines.append(f"{indent}  *[{len(more_ids)} more replies — IDs: {', '.join(more_ids[:5])}{'...' if len(more_ids) > 5 else ''}]*")
                    lines.append("")

    return "\n".join(lines)

def build_comment_tree(things):
    """Build a comment tree from a flat list of things (from morechildren)."""
    by_id = {}
    roots = []
    for thing in things:
        if thing["kind"] == "t1":
            by_id[thing["data"]["name"]] = thing
            thing["data"]["_children"] = []

    for thing in things:
        if thing["kind"] != "t1":
            continue
        parent_id = thing["data"].get("parent_id", "")
        if parent_id in by_id:
            by_id[parent_id]["data"]["_children"].append(thing)
        else:
            roots.append(thing)

    return roots

def render_flat_comment(comment, depth=0):
    if comment.get("kind") != "t1":
        return ""
    data = comment["data"]
    author = data.get("author", "[deleted]")
    body = data.get("body", "[removed]")
    score = data.get("score", 0)
    created = data.get("created_utc", 0)
    indent = "  " * depth
    lines = []
    lines.append(f"{indent}---")
    lines.append(f"{indent}**{author}** | Score: {score} | {ts(created)}")
    lines.append("")
    for line in body.split("\n"):
        lines.append(f"{indent}{line}")
    lines.append("")
    for child in data.get("_children", []):
        lines.append(render_flat_comment(child, depth + 1))
    return "\n".join(lines)

def main():
    print("Fetching main thread JSON...")
    url = f"{BASE_URL}/r/mac/comments/{POST_ID}/bypass_remote_management_on_macbook_pro_after/.json"
    data = fetch_json(url, params={"limit": 500, "depth": 10})

    post_data = data[0]["data"]["children"][0]["data"]
    comments_listing = data[1]["data"]["children"]
    link_fullname = post_data["name"]  # e.g. t3_pi9beh

    title = post_data.get("title", "")
    selftext = post_data.get("selftext", "")
    author = post_data.get("author", "[deleted]")
    score = post_data.get("score", 0)
    num_comments = post_data.get("num_comments", 0)
    created = post_data.get("created_utc", 0)
    permalink = f"https://www.reddit.com{post_data.get('permalink', '')}"

    print(f"Post: {title}")
    print(f"Top-level items: {len(comments_listing)}")

    # Collect all "more" stubs at the top level
    top_more_ids = []
    for child in comments_listing:
        if child.get("kind") == "more":
            top_more_ids.extend(child["data"].get("children", []))

    print(f"Top-level 'more' IDs to fetch: {len(top_more_ids)}")

    # Fetch more top-level comments in batches of 100
    extra_comments = []
    for i in range(0, len(top_more_ids), 100):
        batch = top_more_ids[i:i+100]
        print(f"  Fetching more batch {i//100 + 1} ({len(batch)} IDs)...")
        things = fetch_more_children(link_fullname, batch)
        extra_comments.extend(things)

    # Build the Markdown document
    md_lines = []
    md_lines.append(f"# {title}")
    md_lines.append("")
    md_lines.append(f"**Posted by:** u/{author}  ")
    md_lines.append(f"**Subreddit:** r/mac  ")
    md_lines.append(f"**Date:** {ts(created)}  ")
    md_lines.append(f"**Score:** {score} upvotes | **Comments:** {num_comments}  ")
    md_lines.append(f"**Source:** {permalink}")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Original Post")
    md_lines.append("")
    md_lines.append(selftext)
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## Comments")
    md_lines.append("")
    md_lines.append("> *Comments are ordered by top score. Indentation reflects nesting depth.*")
    md_lines.append("")

    # Render main comments
    comment_count = 0
    for child in comments_listing:
        if child.get("kind") == "t1":
            md_lines.append(render_comment(child, depth=0))
            comment_count += 1

    # Render extra top-level comments from "more"
    if extra_comments:
        tree = build_comment_tree(extra_comments)
        for root in tree:
            md_lines.append(render_flat_comment(root, depth=0))
            comment_count += 1

    print(f"Total comment threads rendered: {comment_count}")

    output = "\n".join(md_lines)
    # Clean up HTML entities
    output = output.replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<").replace("&nbsp;", " ").replace("&#39;", "'").replace("&quot;", '"')

    out_path = "/home/ubuntu/reddit_thread_full_archive.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Written to {out_path}")
    wc = len(output.split("\n"))
    print(f"Total lines: {wc}")

if __name__ == "__main__":
    main()
