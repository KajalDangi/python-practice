string = input("Enter the sentence: ").lower()

vowel = sum(1 for ch in string if ch in "aeiou")
consonant = sum(1 for ch in string if ch.isalpha() and ch not in "aeiou")

if vowel > consonant:
    print("Vowel heavy string")
elif consonant > vowel:
    print("Consonant heavy string")
else:
    print("Balanced string")

n = len(string)

if n == 0:
    print("Empty string")
elif n % 2 == 0:
    print(f"Middle chars are {string[n//2 - 1]} and {string[n//2]}")
else:
    print(f"Middle char is {string[n//2]}")

print(f"OG string: {string}")
print(f"Reversed string: {string[::-1]}")
