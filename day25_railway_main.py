import day25_railway as railway

print("Welcome to the railway ticket booking system!")
print("Please enter the train details:")
railway.train_details()

print("\nNow, let's calculate the ticket price.")
try:
    price_per_ticket = float(input("Enter the price per ticket: "))
    number_of_tickets = int(input("Enter the number of tickets: "))

    if price_per_ticket < 0 or number_of_tickets < 0:
        raise ValueError("Price and number of tickets cannot be negative.")

    total_price = railway.calculate_ticket_price(price_per_ticket, number_of_tickets)
    print(f"The total price for {number_of_tickets} tickets is: {total_price}")
except ValueError as e:
    print(f"Error: {e}")    