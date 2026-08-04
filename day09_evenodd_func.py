def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

x=int(input("Enter a number: "))
if is_even(x):
    print(f"{x} is even")
else:
    print(f"{x} is odd")