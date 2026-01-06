sentence = input("Enter a sentence: ").lower()
d = {}

for ch in sentence:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)
