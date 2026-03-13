import requests
import csv
import sys

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
response.raise_for_status()

data = response.json()

user_id = int(sys.argv[1])
if len(sys.argv) < 2:
    print("Usage: py practice_cli.py <user_id>")
    sys.exit()

with open("filtered_posts_practice.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["userId", "title"])

    for post in data:
        if post["userId"] == user_id and "qui" in post["title"].lower():
            writer.writerow([post["userId"], post["title"]])