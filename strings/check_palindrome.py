given_string = input("Enter the string: ").lower().replace(" ", "")

if given_string == given_string[::-1]:
    print("It is a palindrome")
else:
    print("No")
