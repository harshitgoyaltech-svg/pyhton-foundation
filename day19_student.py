class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class student(person):
    def study(self):
        print(f"{self.name} is studying.")
    
    

    
student1 = student("HARSHIT", 20)
student1.display()  # This will call the display method from the person class
student1.study()  # This will call the study method from the student class