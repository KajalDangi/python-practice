def factorial(n):
    """Return factorial of a non-negative integer."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    try:
        number = int(input("Enter a natural number: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial of {number} is {factorial(number)}")

    except ValueError:
        print("Please enter an integer value.")


if __name__ == "__main__":
    main()