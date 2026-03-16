import csv
import sys

if len(sys.argv) < 2:
    print("Usage: py read_csv.py <city>")
    sys.exit()

city = sys.argv[1]

with open("properties.csv", "r", encoding="utf-8-sig") as f:  # 👈 only change
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames

    with open("filtered_properties.csv", "w", newline="", encoding="utf-8-sig") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row["city"] == city and int(row["price"]) <= 6000000 and row["type"] == "2BHK":
                writer.writerow(row)