class animal:
    def eat(self):
        print("animal can eat")

class dog(animal):
    def bark(self):
        print("dog can bark")

# Creating an instance of the dog class
my_dog = dog()
my_dog.eat()  # This will call the eat method from the animal class
my_dog.bark()  # This will call the bark method from the dog class