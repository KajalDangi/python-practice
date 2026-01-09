"""
ATM Program
Features:
- PIN authentication
- Check balance
- Withdraw money
- Deposit money
- Error handling
- Loop until user exits
"""

PIN = 2006

def pin_check(pin):
    return pin == PIN

def balance_check(balance):
    print(f"Your balance is: ₹{balance}")

def withdraw(amount, balance):
    if amount <= 0:
        print("Amount must be greater than zero.")
    elif amount > balance:
        print(f"Insufficient funds. Available balance: ₹{balance}")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining balance: ₹{balance}")
    return balance

def deposit(amount, balance):
    if amount <= 0:
        print("Deposit amount must be positive.")
    else:
        balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"New balance: ₹{balance}")
    return balance


print("Welcome to the ATM Program!")

balance = 5000

# PIN Authentication
while True:
    try:
        pin_entered = int(input("Enter your PIN: "))
    except ValueError:
        print("PIN must contain numbers only.")
        continue

    if pin_check(pin_entered):
        print("Login successful!\n")
        break
    else:
        print("Incorrect PIN — Try again\n")

# ATM Menu
while True:
    print("\nChoose an option:")
    print("1 Check Balance")
    print("2 Withdraw Money")
    print("3 Deposit Money")
    print("4 Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        balance_check(balance)

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Amount must be a number.")
            continue

        balance = withdraw(amount, balance)

    elif choice == "3":
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Amount must be a number.")
            continue

        balance = deposit(amount, balance)

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1–4.")
