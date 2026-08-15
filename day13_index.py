numbers=[10,20,30,40,50]
index=int(input("Enter the index of the number you want to access (0-4): "))
try:
    print("The number at index", index, "is:", numbers[index])
except IndexError:
    print("Invalid index. Please enter an index between 0 and 4.")