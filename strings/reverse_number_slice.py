def reverse_number(n):
    """Reverse digits of a number using string slicing."""
    return int(str(n)[::-1])


def main():
    try:
        number = int(input("Enter a number: "))
        print(reverse_number(number))
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()