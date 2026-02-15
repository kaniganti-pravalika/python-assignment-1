# Project 1: Hotel Menu Ordering System

# Menu Data
breakfast = {
    1: ("Idli", 30),
    2: ("Dosa", 50),
    3: ("Upma", 40)
}

lunch = {
    1: ("Veg Thali", 120),
    2: ("Paneer Curry", 150),
    3: ("Fried Rice", 100)
}

dinner = {
    1: ("Chapati", 20),
    2: ("Biryani", 180),
    3: ("Noodles", 130)
}

total_bill = 0

while True:
    print("\n===== Welcome to Hotel =====")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Exit")

    choice = int(input("Select category: "))

    if choice == 1:
        menu = breakfast
        print("\n--- Breakfast Menu ---")
    elif choice == 2:
        menu = lunch
        print("\n--- Lunch Menu ---")
    elif choice == 3:
        menu = dinner
        print("\n--- Dinner Menu ---")
    elif choice == 4:
        break
    else:
        print("Invalid choice!")
        continue

    # Display items
    for key, value in menu.items():
        print(key, ".", value[0], "- Rs", value[1])

    while True:
        item = int(input("Select item number: "))
        if item in menu:
            quantity = int(input("Enter quantity: "))
            price = menu[item][1] * quantity
            total_bill += price
            print("Item added to cart. Current Bill: Rs", total_bill)
        else:
            print("Invalid item!")

        more = input("Do you want to order more from this category? (Y/N): ").upper()
        if more != "Y":
            break

# Final Bill Option
print("\n1. View Bill")
print("2. Exit")
final_choice = int(input("Enter choice: "))

if final_choice == 1:
    print("\n===== Final Bill =====")
    print("Total Amount to Pay: Rs", total_bill)
    print("Thank you! Visit Again.")
else:
    print("Thank you! Visit Again.")
