a=[5, 10, 3, 8, 1]
x=int(input("Enter a number to search: "))
if x in a:
    print(f"{x} is present in the list")
else:
    print(f"{x} is not present in the list")