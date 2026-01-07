#Check if a number is prime.
number = int(input("Enter a number: "))
count = 0

if number == 1:
    print("1 is neither prime nor composite")
else:
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is a composite number")