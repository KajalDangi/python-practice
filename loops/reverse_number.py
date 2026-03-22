def reverse_number(n):
    """Reverse digits of an integer using a loop."""
    sign = -1 if n < 0 else 1
    n = abs(n)

    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return sign * reversed_num


def main():
    try:
        number = int(input("Enter a number: "))
        print(reverse_number(number))
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()