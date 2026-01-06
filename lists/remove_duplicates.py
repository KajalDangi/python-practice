numbers = input("Enter the numbers: ").split()
lis = []

for n in numbers:
    if int(n) not in lis:
        lis.append(int(n))

print(lis)

