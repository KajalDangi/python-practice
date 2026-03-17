def generate_fibonacci(n):
    """Generate Fibonacci series up to n terms."""
    series = []

    for i in range(n):
        if i < 2:
            series.append(i)
        else:
            series.append(series[i - 1] + series[i - 2])

    return series


def main():
    try:
        n = int(input("Enter the number of terms: "))

        if n <= 0:
            print("Terms must be positive.")
        else:
            print(generate_fibonacci(n))

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()