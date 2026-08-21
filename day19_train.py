class train:
    def __init__(self, name,number,method):
        self.name = name
        self.number = number
        self.method = method

    def display(self):
        print(f"Name: {self.name}, Number: {self.number}, Method: {self.method}")

class express_train(train):
    def __init__(self, name, number, method, speed):
        super().__init__(name, number, method)
        self.speed = speed

    def display(self):
        super().display()
        print(f"Speed: {self.speed}")
        
train1 = express_train("Shatabdi Express", 12001, "Electric", "130 km/h")
train2 = express_train("Rajdhani Express", 12951, "Electric", "150 km/h")
train1.display()  # This will call the display method from the express_train class
train2.display()  # This will call the display method from the express_train class