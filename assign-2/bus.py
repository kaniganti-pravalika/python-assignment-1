# Project 2: Bus Ticket Booking System

routes = {
    1: {"route": "City A to City B", "price": 250, "seats": 10},
    2: {"route": "City B to City C", "price": 300, "seats": 8},
    3: {"route": "City A to City C", "price": 400, "seats": 5}
}

total_bill = 0

while True:
    print("\n===== Bus Ticket Booking System =====")
    print("Available Routes:")

    for key, value in routes.items():
        print(f"{key}. {value['route']} - Rs {value['price']} (Seats Available: {value['seats']})")

    print("4. Exit")

    choice = int(input("Select route: "))

    if choice == 4:
        break

    if choice in routes:
        selected_route = routes[choice]

        tickets = int(input("Enter number of tickets: "))

        # Seat validation
        if tickets <= selected_route["seats"]:
            cost = tickets * selected_route["price"]
            total_bill += cost
            selected_route["seats"] -= tickets

            print("Booking Successful!")
            print("Cost for this booking: Rs", cost)
            print("Remaining Seats:", selected_route["seats"])
        else:
            print("Error: Not enough seats available!")
    else:
        print("Invalid route selection!")

    again = input("Do you want to book another ticket? (Y/N): ").upper()
    if again != "Y":
        break

# Final Bill Summary
print("\n===== Final Bill Summary =====")
print("Total Amount to Pay: Rs", total_bill)
print("Thank you for booking with us!")
