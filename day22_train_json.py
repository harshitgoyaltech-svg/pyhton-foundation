import json

train = {
    "name": "Vande Bharat Express",
    "source": "New Delhi",
    "destination": "varanasi",
    "departure": "5:00 AM",
    "arrival": "2:00 PM",
    "speed": 130,
    "number_of_coaches": 16,
    "train_number": 12345
}
with open("train.json", "w") as file:
    json.dump(train, file, indent=4)

print("JSON file created successfully.")