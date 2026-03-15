def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    try:
        year = int(input("Enter the year: "))

        if is_leap(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

    except ValueError:
        print("Please enter a valid integer year.")


main()
