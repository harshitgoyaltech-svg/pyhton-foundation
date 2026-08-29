import json

with open("train.json", "r") as file:
    train_data = json.load(file)

print(train_data)
print("Name:", train_data["name"])
print("Train Number:", train_data["train_number"])
print("Source:", train_data["source"])
print("Destination:", train_data["destination"])
print("Departure:", train_data["departure"])
print("Arrival:", train_data["arrival"])
print("Speed:", train_data["speed"])
print("Number of Coaches:", train_data["number_of_coaches"])
