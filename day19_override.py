class animal:
    def sound(self):
        print("animal makes a sound")

class dog(animal):
    def sound(self):
        print("dog barks")

class cat(animal):
    def sound(self):
        print("cat meows")

dog1 = dog()
cat1 = cat()
dog1.sound()  # This will call the sound method from the dog class
cat1.sound()  # This will call the sound method from the cat class