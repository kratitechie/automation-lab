import requests
import csv 

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
USERS_URL = "https://jsonplaceholder.typicode.com/users"

OUTPUT_FILE = "filtered_posts.csv"


def fetch_posts():
    response = requests.get(POSTS_URL)
    response.raise_for_status()
    return response.json()

def fetch_users():
    response = requests.get(USERS_URL)
    response.raise_for_status()
    return response.json()

try:
    posts = fetch_posts()
    users = fetch_users()
except Exception as e:
    print("Failed to fetch API data:", e)
    exit(1)

user_id_to_filter = int(input("Enter userId to filter (1–10): "))

user_lookup= {}
for user in users:
    user_lookup[user["id"]]=user["name"]

joined_posts = []
for post in posts:
    user_id = post["userId"]
    user_name = user_lookup.get(user_id, "Unknown")

    joined_posts.append({
        "post_id": post["id"],
        "user_id": user_id,
        "user_name": user_name,
        "title": post["title"]
    })

    user_id_to_filter = 3  # change this to test
filtered_posts = []

for item in joined_posts:
    if item["user_id"] == user_id_to_filter:
        filtered_posts.append(item)

# Print 5 results to verify
for item in filtered_posts[:5]:
    print(item)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["post_id", "user_id", "user_name", "title"])

    for item in filtered_posts:
        writer.writerow([
            item["post_id"],
            item["user_id"],
            item["user_name"],
            item["title"]
        ])

print(f"Saved {len(filtered_posts)} posts to {OUTPUT_FILE}")