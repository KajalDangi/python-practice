"""
ATM Program
Features:
 PIN authentication
 Check balance
 Withdraw money
 Deposit money
 Error handling
 Loop until user exits
"""

print(" Welcome to the ATM Program!")

PIN = 2006
balance = 5000
while True:
    try:
        pin_entered = int(input("Enter your PIN: "))
    except ValueError:
        print("PIN must be numbers only.")
        continue

    if pin_entered == PIN:
        print("Login successful \n")
        break
    else:
        print("Incorrect PIN — Try again\n")


while True:
    print("\nChoose an option:")
    print("1  Check Balance")
    print("2 Withdraw Money")
    print("3️  Deposit Money")
    print("4 Exit")

    choice = input("Enter your choice (1-4): ")

    # Check Balance
    if choice == "1":
        print(f" Your balance is: ₹{balance}")

    # Withdraw
    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Amount must be a number.")
            continue

        if amount <= 0:
            print(" Amount must be greater than zero.")
        elif amount > balance:
            print(f" Insufficient funds. Available balance: ₹{balance}")
        else:
            balance -= amount
            print(f" ₹{amount} withdrawn successfully.")
            print(f" Remaining balance: ₹{balance}")

    # Deposit
    elif choice == "3":
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Amount must be a number.")
            continue

        if amount <= 0:
            print(" Deposit amount must be positive.")
        else:
            balance += amount
            print(f" ₹{amount} deposited successfully.")
            print(f" New balance: ₹{balance}")

    # Exit
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print(" Invalid option. Please choose between 1–4.")
