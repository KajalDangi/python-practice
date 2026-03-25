"""
Program: Remove Duplicate Words from a Sentence

Description:
This program removes duplicate words from a sentence using Python sets.
The comparison is case-insensitive.
"""

def unique_words(words):
    """Return a set of unique words."""
    return set(word.lower() for word in words)


def main():
    sentence = input("Enter the sentence: ")
    words = sentence.split()

    print("Unique words:", unique_words(words))


if __name__ == "__main__":
    main()