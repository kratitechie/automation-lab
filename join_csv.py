import csv

EMP_FILE = "employees.csv"
ATT_FILE = "attendance.csv"
OUT_FILE = "report.csv"

# Read employees.csv
with open(EMP_FILE, newline="", encoding="utf-8") as f:
    employees = list(csv.DictReader(f))

# Read attendance.csv
with open(ATT_FILE, newline="", encoding="utf-8") as f:
    attendance = list(csv.DictReader(f))

# Build lookup dict: id -> name
employee_lookup = {}
for e in employees:
    employee_lookup[e["id"]] = e["name"]

# Join data and write report.csv
with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["employeeId", "name", "hours"])

    for attendee in attendance:
        emp_id = attendee["employeeId"]
        hours = attendee["hours"]

        name = employee_lookup.get(emp_id, "Unknown")

        writer.writerow([emp_id, name, hours])

print("Saved report.csv successfully!")

print("Employees:", employees)
print("Attendance:", attendance)