"""
Shopping Cart Program
Features:
- View items
- Check item price
- Billing system
"""

items = {
    "tshirt": 500,
    "shirt": 800,
    "track pants": 1000,
    "jeans": 900
}

while True:
    print("\n1. View Items")
    print("2. Check Price")
    print("3. Billing")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for item, price in items.items():
            print(item, "-", price)

    elif choice == "2":
        name = input("Enter item name: ").lower()
        if name in items:
            print("Price:", items[name])
        else:
            print("Item not available.")

    elif choice == "3":
        total = 0
        count = int(input("Number of different items: "))

        for i in range(count):
            name = input("Enter item name: ").lower()
            qty = int(input("Enter quantity: "))

            if name in items:
                cost = items[name] * qty
                total += cost
                print(name, "=", cost)
            else:
                print("Item not available.")

        print("Total bill:", total)

    elif choice == "4":
        print("Thank you for shopping.")
        break

    else:
        print("Invalid option.")


