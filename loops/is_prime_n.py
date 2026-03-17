def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    try:
        number = int(input("Enter the number: "))

        if number == 0:
            print("Zero is neither prime nor non-prime.")
        elif is_prime(number):
            print(f"{number} is a Prime number.")
        else:
            print(f"{number} is not a Prime number.")

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()