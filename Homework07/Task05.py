import json

table = [
{"name": "Ana", "grades": [90, 80, 95]},
{"name": "Beka", "grades": [70, 85, 88]},
{"name": "Nino", "grades": [100, 95, 99]}
]

max_grade = 0
max_name = None

for person in table:
    grades = person["grades"]
    average = sum(grades) / len(grades)
    
    if average > max_grade:
        max_grade = average
        max_name = person["name"]

print(f"best student: {person["name"]}. Average grade: {max_grade}")
