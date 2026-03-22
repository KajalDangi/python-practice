def number_type(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    return "zero"


def main():
    try:
        n = int(input("Enter the number: "))
        result = number_type(n)

        if result == "zero":
            print("Zero is neither positive nor negative.")
        else:
            print(f"{n} is a {result} number.")

    except ValueError:
        print("Please enter a valid integer.")



if __name__ == "__main__":
    main()