import requests
import csv

url =  "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

with open ("api_fetch_users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "email", "city"])
    for i in data:
        writer.writerow([i["id"], i["name"], i["email"], i["address"]["city"]])


print("number of users:\n", len(data))
print("name of the first users is:\n", data [0]["name"])
print("Email id of last user:\n", data[-1]["email"])

