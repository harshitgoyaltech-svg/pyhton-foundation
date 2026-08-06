fruits={"apple": 150, "banana": 100, "orange": 180}
fruit=input("Enter the fruit name: ")
if fruit in fruits:
    print(f"The price of {fruit} is {fruits[fruit]}")
else:
    print("Fruit not found.")