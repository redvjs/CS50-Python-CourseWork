import csv

students =[]

with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"], "house": row["house"]})
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} lives at {student['home']} and belongs to {student['house']}")