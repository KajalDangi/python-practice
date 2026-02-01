# Auto Calendar Generator (Python)
# Author: Kajal Dangi
# Description: Prints a monthly calendar for a given year and month

def year_in():
    while True:
        try:
            return int(input("Enter the year: "))
        except ValueError:
            print("Year must be an integer.")


def month_in(months):
    while True:
        month = input("Enter the month: ").title()
        if month in months:
            return month
        print("Invalid month name.")


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(month, year, months, days_list):
    if month == "February" and is_leap(year):
        return 29
    return days_list[months.index(month)]


def starting_day(year, month, months, days_list):
    """
    Calculates the weekday index of the first day of the given month.
    Reference: 1 Jan 1900 = Monday
    """
    total_days = 0

    for y in range(1900, year):
        total_days += 366 if is_leap(y) else 365

    for m in months[:months.index(month)]:
        total_days += days_in_month(m, year, months, days_list)

    return total_days % 7


def print_month(year, month, months, days_list, days):
    start = starting_day(year, month, months, days_list)
    total_days = days_in_month(month, year, months, days_list)

    print("\n" + "_" * 50)
    print(f"{month.upper()} {year}".center(50))
    print("_" * 50)

    for d in days:
        print(f"{d:^7}", end="")
    print()

    for _ in range(start):
        print(" " * 7, end="")

    for day in range(1, total_days + 1):
        print(f"{day:^7}", end="")
        if (start + day) % 7 == 0:
            print()


# ---------------- MAIN PROGRAM ---------------- #

days = ["MON", "TUES", "WED", "THURS", "FRI", "SAT", "SUN"]
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print("WELCOME TO AUTO CALENDAR GENERATOR")
print("-" * 50)

year = year_in()
month = month_in(months)

print_month(year, month, months, days_list, days)