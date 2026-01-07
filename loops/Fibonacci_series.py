#Fibonacci series up to N terms. (0, 1, 1, 2, 3, 5, 8, 13, ...)
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    fib = []
    for i in range(n):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    print(fib)
