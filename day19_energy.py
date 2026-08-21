class energy_source:
    def __init__(self, name):
        self.name = name

    def show_source(self):
        print(f"Energy Source: {self.name}")

class SolarEnergy(energy_source):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity

    def show_capacity(self):
        print(f"Capacity: {self.capacity} kW")

solar1= SolarEnergy("Solar Panel", 5)
solar2= SolarEnergy("Solar Roof", 10)
solar1.show_source()  # This will call the show_source method from the energy_source class
solar1.show_capacity()  # This will call the show_capacity method from the SolarEnergy class
solar2.show_source()  # This will call the show_source method from the energy_source class
solar2.show_capacity()  # This will call the show_capacity method from the SolarEnergy class