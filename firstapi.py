import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

posts = response.json()

with open("api_posts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "title", "body"])

    for post in posts:
        writer.writerow([post["id"], post["title"], post["body"]])

print("Saved api_posts.csv")
