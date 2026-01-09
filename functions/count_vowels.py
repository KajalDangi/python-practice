def count_vowels(s):
    """Returns the number of vowels in a given string"""
    counter = 0
    for i in s.lower():
        if i in "aeiou":
            counter += 1
    return counter


sen=input("Enter the sentence: ")
print(count_vowels(sen))