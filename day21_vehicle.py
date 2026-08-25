class train:
    def move(self):
        print("train moves on railway tracks")

class car:
    def move(self):
        print("car moves on road")

class airplane:
    def move(self):
        print("airplane flies in the air")

vehicles = [train(),car(),airplane()]
for vehicle in vehicles:
    vehicle.move()