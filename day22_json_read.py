import json

with open("student.json", "r") as file:
    student_data = json.load(file)

print(student_data)
print("Name:", student_data["name"])
print("Branch:", student_data["branch"])
print("Year:", student_data["year"])