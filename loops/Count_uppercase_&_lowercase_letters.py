#Count uppercase & lowercase letters.
sentence = input("Provide a sentence: ")

count_u =sum(1 for ch in sentence if ch.isupper())
count_l =sum(1 for ch in sentence if ch.islower())

print("Uppercase:", count_u)
print("Lowercase:", count_l)
