# Reads a CSV file using csv.reader

import csv

students = []

# note the formatting of Harry's home in students1.csv
with open("students1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})
'''
    for name, home in reader:
        students.append({"name": name, "home": home})
'''

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
