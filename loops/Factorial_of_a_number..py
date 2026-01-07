#Factorial of a number.
number = int(input("Enter a natural number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fac = 1
    for i in range(1, number + 1):
        fac *= i
    print(f"Factorial of {number} is {fac}")