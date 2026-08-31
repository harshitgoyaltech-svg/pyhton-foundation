import csv

with open("trains.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Train Name", "Train Number", "Source", "Destination","speed"])
    writer.writerow(["Rajdhani Express", 12345, "New Delhi", "Mumbai", 180])
    writer.writerow(["Shatabdi Express", 67890, "Chennai", "Bangalore", 160])
    writer.writerow(["Duronto Express", 54321, "Kolkata", "Hyderabad", 140])

print("CSV file 'trains.csv' has been created and data written successfully.")

with open("trains.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)