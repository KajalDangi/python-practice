numbers = input("Enter the numbers: ").split()
lis = []

for n in numbers:
    lis.append(int(n))

print(lis)
print(max(lis))
print(min(lis))
