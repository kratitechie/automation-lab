students = [
    {"id": 1, "name": "A"},
    {"id": 2, "name": "B"},
]

marks = [
    {"studentId": 1, "score": 90},
    {"studentId": 2, "score": 75},
    {"studentId": 3, "score": 60},  # missing student
]

# TODO 1: Build lookup dict (id -> name)
student_lookup = {}
for student in students:
    student_lookup[student["id"]] = student["name"]

# TODO 2: Use lookup to print name + score
for mark in marks:
    name = student_lookup.get(mark["studentId"], "Unknown")
    print(f"{name} scored {mark['score']}")