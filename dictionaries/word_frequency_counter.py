#Word Frequency Counter

sentence = input("Enter a sentence: ").split()
book = {}

for word in sentence:
    if word in book:
        book[word] += 1
    else:
        book[word] = 1

print(book)
