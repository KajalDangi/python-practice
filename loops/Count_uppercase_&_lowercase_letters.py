#Count uppercase & lowercase letters.
sentence = input("Provide a sentence: ")

count_u = 0
count_l = 0

for ch in sentence:
    if ch.isupper():
        count_u += 1
    elif ch.islower():
        count_l += 1

print("Uppercase:", count_u)
print("Lowercase:", count_l)
