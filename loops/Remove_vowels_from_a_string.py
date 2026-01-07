#Remove all vowels from a string.
s = input("Enter the string: ")
result = ""

for ch in s:
    if ch not in "aeiouAEIOU":
        result += ch

print(result)