# Reads as dictionary of columns using csv.DictReader
# instead of list of columns using csv.reader

import csv

students = []

# csv.DictReader requires students2.csv to contain headers
# allows dragging columns around in Excel
with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
#        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
