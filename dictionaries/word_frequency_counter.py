"""
Program: Word Frequency Counter
"""

def word_frequency(word_list):

    word_freq = {}

    for word in word_list:
        word = word.lower()
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print(word_frequency(words))


if __name__ == "__main__":
    main()