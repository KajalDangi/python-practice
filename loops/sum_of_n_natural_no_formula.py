def sum_natural_numbers(n):
    return n * (n + 1) // 2


def main():
    try:
        n = int(input("Enter the number: "))
        print(sum_natural_numbers(n))
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()