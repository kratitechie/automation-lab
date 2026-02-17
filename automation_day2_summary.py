import csv

cleaned_emails = []
city_count = {}
unique_cities = set()

with open("api_fetch_users.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# clean emails
for row in rows:
    email = row["email"]
    clean_email = email.strip().lower()
    cleaned_emails.append(clean_email)

# count cities
for row in rows:
    city = row["city"]
    city_count[city] = city_count.get(city, 0) + 1

# collect unique cities
for row in rows:
    unique_cities.add(row["city"])

sorted_cities = sorted(unique_cities)
cities_line = ", ".join(sorted_cities)

# write summary
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(f"Total users: {len(rows)}\n")
    f.write(f"First user: {rows[0]['name']}\n")
    f.write(f"Last user email: {rows[-1]['email']}\n")
    f.write(f"Cities (unique): {cities_line}\n")

    biz_count = 0
    for row in rows:
        if row["email"].lower().endswith(".biz"):
            biz_count += 1

    f.write(f"Users with .biz email: {biz_count}\n")

print("summary.txt created")

print("Unique cities (first 5):", sorted_cities[:5])
print("City counts:", city_count)
print("First 3 cleaned emails:", cleaned_emails[:3])
print("Total users:", len(rows))
print("First row:", rows[0])
