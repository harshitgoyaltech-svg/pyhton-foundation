try:
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    result=a/b
    print(f"the result of {a}/{b} is {result}")
except ZeroDivisionError:
    print("error: division by zero is not allowed.")
except ValueError:
    print("invalid input. please enter a valid integer.")