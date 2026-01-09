def r_sum(n):
    """Returns sum of first n natural numbers using recursion"""
    if n < 0:
        return "Invalid input"
    if n == 0:
        return 0
    return n + r_sum(n - 1)


number=int(input("Enter a number: "))
print(r_sum(number))