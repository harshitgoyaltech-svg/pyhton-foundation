class train:
    def __init__(self, name, number, destination):
        self.name = name
        self.number = number
        self.destination = destination

    def introduce(self):
        print(f"Train name is {self.name}, Train number is {self.number}, and destination is {self.destination}.")

train1 = train("Shatabdi Express", 12001, "New Delhi")
train2 = train("Rajdhani Express", 12951, "Mumbai")

train1.introduce()
train2.introduce()