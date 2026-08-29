import json

energy_sources = [
    {
        "source": "Solar",
        "capacity": 500
    },
    {
        "source": "Wind",
        "capacity": 300
    },
    {
        "source": "Hydro",
        "capacity": 800
    }
]

with open("energy.json", "w") as file:
    json.dump(energy_sources, file, indent=4)

print("JSON file created successfully.")