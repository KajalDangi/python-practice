def print_table(number, limit=10):
    for i in range(1, limit + 1):
        print(f"{number} × {i} = {number * i}")


def main():
    try:
        number = int(input("Enter a number: "))
        print_table(number)
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()