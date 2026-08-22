class train:
    def __init__(self, train_name, private_speed):
        self.train_name = train_name
        self.__private_speed = private_speed  # Private attribute
    def get_speed(self):
        return self.__private_speed  # Getter method to access the private attribute
    def set_speed(self, speed):
        if speed > 0:
            self.__private_speed = speed  # Setter method to modify the private attribute
        else:
            print("Speed must be a positive value.")

train1 = train("Shatabdi Express", 100)
print(train1.get_speed())  # Output: 100
train1.set_speed(120)  # Valid speed
print(train1.get_speed())  # Output: 120
train1.set_speed(-50)  # Invalid speed
print(train1.get_speed())  # Output: 120