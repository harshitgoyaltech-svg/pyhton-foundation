class dog:
    def sound(self):
        print("Dog barks")
class cat:
    def sound(self):
        print("cat meows")

animals = [dog(),cat()]
for animal in animals:
    animal.sound()