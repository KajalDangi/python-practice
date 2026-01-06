given_string = input("Specify a string to check: ").lower()

if given_string == given_string[::-1]:
    print("Yes, it is a palindrome")
else:
    print("It is not a palindrome")
