import requests
import csv
from datetime import datetime
import sys

if len(sys.argv) != 3:
    print("Usage: py report_generator.py input.csv output.csv")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    response = requests.get(POSTS_URL)
    response.raise_for_status()
    return response.json()

def filter_posts(posts, user_id=None, keyword=None):
    filtered = []
    for post in posts:
        if user_id is not None and post["userId"] != user_id:
            continue

        if keyword is not None and keyword.lower() not in post["title"].lower():
            continue

        filtered.append(post)

    return filtered

def write_csv(posts, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["userId", "id", "title", "body"])

        for post in posts:
            writer.writerow([
                post["userId"],
                post["id"],
                post["title"],
                post["body"],
            ])

def main():
    try:
        posts = fetch_posts()

        # 🔧 Configurable rules (change these)
        user_id_to_report = 3          # set None to disable user filter
        keyword_in_title = "qui"       # set None to disable keyword filter

        filtered_posts = filter_posts(
            posts,
            user_id=user_id_to_report,
            keyword=keyword_in_title
        )

        write_csv(filtered_posts, output_file)
        print(f"✅ Report generated: {output_file}")
        print(f"📊 Rows in report: {len(filtered_posts)}")
    except Exception as e:
        print("❌ Failed to generate report:", e)

if __name__ == "__main__":
    main()