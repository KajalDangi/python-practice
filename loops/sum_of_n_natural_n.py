#Sum of first N natural numbers.
N = int(input("Enter a number: "))
total = 0
i = 1

while i <= N:
    total += i
    i += 1

print(total)