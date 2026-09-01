try:
    capacity=int(input("enter the capacity of the battery in mAh:"))

    if capacity<=0:
        raise ValueError("capacity cannot be negative.")
    else:
        print(f"the capacity of the battery is {capacity} mAh.")
except ValueError:
    print("invalid input. please enter a valid integer.")