import csv
with open("energy.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Capacity","location"])
    writer.writerow(["Solar", 500, "Desert"])
    writer.writerow(["Wind", 300, "Coastal"])
    writer.writerow(["Hydro", 200, "Mountain"])

print("CSV file 'energy.csv' has been created and data written successfully.")

with open("energy.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)