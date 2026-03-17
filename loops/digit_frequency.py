def digit_frequency(num):
    """Return frequency of each digit in a number."""
    counter = {}

    for digit in str(abs(num)):
        counter[digit] = counter.get(digit, 0) + 1

    return counter

def main():
    try:
        number = int(input("Enter the number: "))
        print(digit_frequency(number))
    except ValueError:
        print("Please enter valid integral value.")