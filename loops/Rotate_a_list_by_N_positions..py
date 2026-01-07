#Rotate a list by N positions.
n = int(input("Enter a number: "))
l = [12,23,34,5,6,7,3,2,1]

n = n % len(l)

l1 = l[:n]
l2 = l[n:]

print(l2 + l1)
