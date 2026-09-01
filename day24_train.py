try:
    number_of_tickets = int(input("Enter the number of tickets: "))
   

    if number_of_tickets <= 0:
        raise ValueError("Number of tickets cannot be negative.")

    else:
        print(f"You have purchased {number_of_tickets} tickets.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
