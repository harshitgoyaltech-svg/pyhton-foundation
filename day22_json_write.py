import json 

student = {
    "name": "Harshit",
    "branch": "DATA SCIENCE",
    "year": 2,
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")