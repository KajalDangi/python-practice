first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)

if second_number != 0:
    print("Division:", first_number / second_number)
else:
    print("Division: Error! Cannot divide by zero.")
