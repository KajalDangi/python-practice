def sum_natural_numbers(n):
    total = 0
    for num in range(1, n + 1):
        total += num
    return total


def main():
    try:
        n = int(input("Enter a number: "))
        print(sum_natural_numbers(n))
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()