class student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks=marks
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")

student = student("HARSHIT", 85)
print(student.get_marks())  # Output: 85
student.set_marks(92)  # Valid marks
print(student.get_marks())  # Output: 92
student.set_marks(105)  # Invalid marks
print(student.get_marks())  # Output: 92