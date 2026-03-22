"""
Program: Character Frequency Counter
"""

def char_frequency(text):

    char_freq = {}

    for ch in text.lower():
        char_freq[ch] = char_freq.get(ch, 0) + 1

    return char_freq


def main():
    sentence = input("Enter a sentence: ")
    print(char_frequency(sentence))


if __name__ == "__main__":
    main()