import requests
import json
import time

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; RedditScraper/1.0)"}

POST_URL = "https://www.reddit.com/r/mac/comments/pi9beh/bypass_remote_management_on_macbook_pro_after/.json?limit=500&depth=10"

def fetch_json(url):
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.json()

def render_comment(comment, depth=0):
    """Recursively render a comment and its replies as Markdown."""
    indent = "  " * depth
    if comment.get("kind") != "t1":
        return ""

    data = comment["data"]
    author = data.get("author", "[deleted]")
    body = data.get("body", "[removed]")
    score = data.get("score", 0)
    created = data.get("created_utc", 0)

    # Format timestamp
    import datetime
    ts = datetime.datetime.utcfromtimestamp(created).strftime("%Y-%m-%d %H:%M UTC")

    lines = []
    # Comment header
    lines.append(f"{indent}---")
    lines.append(f"{indent}**{author}** | Score: {score} | {ts}")
    lines.append("")
    # Comment body — indent each line
    for line in body.split("\n"):
        lines.append(f"{indent}{line}")
    lines.append("")

    # Recurse into replies
    replies = data.get("replies", "")
    if replies and isinstance(replies, dict):
        children = replies.get("data", {}).get("children", [])
        for child in children:
            lines.append(render_comment(child, depth + 1))

    return "\n".join(lines)

def main():
    print("Fetching thread JSON...")
    data = fetch_json(POST_URL)

    # data[0] = post listing, data[1] = comments listing
    post_data = data[0]["data"]["children"][0]["data"]
    comments_listing = data[1]["data"]["children"]

    title = post_data.get("title", "")
    selftext = post_data.get("selftext", "")
    author = post_data.get("author", "[deleted]")
    score = post_data.get("score", 0)
    num_comments = post_data.get("num_comments", 0)
    created = post_data.get("created_utc", 0)
    url = f"https://www.reddit.com{post_data.get('permalink', '')}"

    import datetime
    ts = datetime.datetime.utcfromtimestamp(created).strftime("%Y-%m-%d %H:%M UTC")

    md_lines = []
    md_lines.append(f"# {title}")
    md_lines.append("")
    md_lines.append(f"**Posted by:** u/{author}  ")
    md_lines.append(f"**Subreddit:** r/mac  ")
    md_lines.append(f"**Date:** {ts}  ")
    md_lines.append(f"**Score:** {score} upvotes | **Comments:** {num_comments}  ")
    md_lines.append(f"**Source:** {url}")
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

    for child in comments_listing:
        if child.get("kind") == "t1":
            md_lines.append(render_comment(child, depth=0))
        elif child.get("kind") == "more":
            ids = child["data"].get("children", [])
            if ids:
                md_lines.append(f"*[{len(ids)} more comments not loaded]*")
                md_lines.append("")

    output = "\n".join(md_lines)
    with open("/home/ubuntu/reddit_thread_archive.md", "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Done. Written to /home/ubuntu/reddit_thread_archive.md")
    print(f"Total top-level comment objects processed: {len(comments_listing)}")

if __name__ == "__main__":
    main()
