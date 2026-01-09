def total_sum(*numbers):
    """Returns the sum of all numbers passed as arguments"""
    total = 0
    for n in numbers:
        total += n
    return total

nums = input("Enter numbers separated by space: ").split()
numbers = []

for n in nums:
    numbers.append(int(n))

print(total_sum(*numbers))
