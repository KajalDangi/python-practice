"""
Password Validator
Rules:
- Minimum 8 characters
- At least one uppercase letter
- At least one digit
- At least one special character
"""

import string

password = input("Enter password: ")

has_upper = False
has_digit = False
has_special = False

if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in string.punctuation:
            has_special = True

    if has_upper and has_digit and has_special:
        print("Valid password.")
    else:
        print("Invalid password.")
        if not has_upper:
            print("Missing uppercase letter.")
        if not has_digit:
            print("Missing digit.")
        if not has_special:
            print("Missing special character.")


