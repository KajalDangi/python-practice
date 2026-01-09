def power(base, exponent=2):
    """Returns base raised to the given exponent (default exponent is 2)"""
    return base ** exponent


b = int(input("Enter base: "))
e = input("Enter exponent (press Enter for square): ")

if e == "":
    print(power(b))
else:
    print(power(b, int(e)))
