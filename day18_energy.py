class solar_panel:
    def __init__(self, capacity, location):
        self.capacity = capacity
        self.location = location

    def introduce(self):
        print(f"Solar panel capacity is {self.capacity} and it is located in {self.location}.")

solar_panel1 = solar_panel("500 kW", "VELLORE")
solar_panel2 = solar_panel("1 MW", "CHENNAI")
solar_panel1.introduce()
solar_panel2.introduce()