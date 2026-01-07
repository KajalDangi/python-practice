#Print multiplication table of a number
try:
    number = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")
except ValueError:
    print("Please enter a valid number!")