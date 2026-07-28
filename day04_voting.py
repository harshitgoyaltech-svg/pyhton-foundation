age=int(input("Enter your age: "))
id=input("Do you have a valid ID? (yes/no): ")
if age>=18 and id=="yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")