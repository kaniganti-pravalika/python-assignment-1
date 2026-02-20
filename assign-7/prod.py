
def purchase_product(inventory, product, quantity):
    if product in inventory:
        if inventory[product] >= quantity:
            inventory[product] -= quantity
            print("Purchase successful")
            print(f"Remaining {product}: {inventory[product]}")
        else:
            print("Insufficient stock")
    else:
        print("Product not found")

inventory = {
    "Pen": 10,
    "Notebook": 5,
    "Pencil": 20
}


product_name = input("Enter product name: ")
quantity = int(input(f"Enter quantity for {product_name}: "))

purchase_product(inventory, product_name, quantity)