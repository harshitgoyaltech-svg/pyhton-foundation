import json

with open("energy.json", "r") as file:
    energy_data = json.load(file)

print(energy_data)
print("Sources:", [source['source'] for source in energy_data])
print("Capacities:", [source['capacity'] for source in energy_data])    