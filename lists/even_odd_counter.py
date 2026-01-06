numbers = input("Enter the numbers: ").split()
lis = []

for n in numbers:
    lis.append(int(n))

e_count = 0
for n in lis:
    if n % 2 == 0:
        e_count += 1

print(f"Number of even numbers is {e_count}")
print(f"Number of odd numbers is {len(lis) - e_count}")
