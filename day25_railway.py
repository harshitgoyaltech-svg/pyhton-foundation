def train_details():
    train_number = input("Enter the train number: ")
    train_name = input("Enter the train name: ")
    source_station = input("Enter the source station: ")
    destination_station = input("Enter the destination station: ")
    departure_time = input("Enter the departure time (HH:MM): ")
    arrival_time = input("Enter the arrival time (HH:MM): ")

    print("\nTrain Details:")
    print(f"Train Number: {train_number}")
    print(f"Train Name: {train_name}") 
    print(f"Source Station: {source_station}")
    print(f"Destination Station: {destination_station}")
    print(f"Departure Time: {departure_time}")
    print(f"Arrival Time: {arrival_time}")

def calculate_ticket_price(price,tickets):
    total_price = price * tickets
    return total_price