class person:
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,branch):
        super().__init__(name)
        self.branch=branch

    def display(self):
        print(f"Name: {self.name}, Branch: {self.branch}")

student = student("HARSHIT", "DATA SCIENCE")
student.display()