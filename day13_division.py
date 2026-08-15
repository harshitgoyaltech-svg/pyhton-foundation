try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("The result of the division is:", result)
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")