def print_table(number, limit=10):
    """Print multiplication table of a number."""
    for i in range(1, limit + 1):
        print(f"{number} × {i} = {number * i}")


def main():
    try:
        number = int(input("Enter a number: "))

        for i in range(1, number + 1):
            print_table(i)
            print("-" * 20)

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()