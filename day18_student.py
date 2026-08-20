class student:
    def __init__(self, name, branch, age):
        self.name = name
        self.branch = branch
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Branch: {self.branch}, Age: {self.age}")

student1=student("Harshit","CSE Data Science",19)
student2=student("Harsh","Electrical and Electronics engineering",20)

student1.display()
student2.display()