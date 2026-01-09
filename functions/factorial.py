def fact(num):
    """Returns factorial of a non-negative integer using recursion"""
    if num < 0:
        return "Factorial is not defined for negative numbers"
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)

n = int(input("Enter a number: "))
print(fact(n))
