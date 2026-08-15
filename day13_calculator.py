try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator. Please enter one of +, -, *, /.")
    print("The result of the operation is:", result)
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
