class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    def introduce(self):
        print("Hello, I am a calculator.")

calc = calculator()
result1 = calc.add(10, 5)
result2 = calc.subtract(10, 5)
result3 = calc.multiply(10, 5)
result4 = calc.divide(10, 5)

calc.introduce()
print("Addition:", result1)
print("Subtraction:", result2)
print("Multiplication:", result3)
print("Division:", result4)