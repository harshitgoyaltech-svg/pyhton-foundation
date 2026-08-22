class SolarPanel:
    def __init__(self, location, private_capacity):
        self.location = location
        self.__private_capacity = private_capacity

    def get_capacity(self):
        return self.__private_capacity

    def set_capacity(self, capacity):
        if capacity > 0:
            self.__private_capacity = capacity
        else:
            print("Capacity must be a positive value.")         

sp1 = SolarPanel("Rooftop", 5)
print(sp1.get_capacity())  # Output: 5
sp1.set_capacity(10)
print(sp1.get_capacity())  # Output: 10 
sp1.set_capacity(-3)  # Invalid capacity
print(sp1.get_capacity())  # Output: 10