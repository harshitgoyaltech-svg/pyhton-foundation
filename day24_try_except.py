try:
    number=int(input("enter the number:"))
    print(f"you entered: {number}")
except ValueError:
    print("invalid input. please enter a valid integer.")