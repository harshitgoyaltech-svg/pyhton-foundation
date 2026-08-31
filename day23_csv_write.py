import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks", "Branch"])
    writer.writerow(["HARSHIT", 90, "DATA SCIENCE"])
    writer.writerow(["PRANJAL", 85, "CSE"])
    writer.writerow(["BILLODA", 95, "MECHANICAL"])

print("CSV file 'students.csv' has been created and data written successfully.")