"""
Program: Find Common Words Between Two Sentences

Description:
This program finds the common words between two sentences using Python sets.
The comparison is case-insensitive.
"""

def common_words(list1, list2):
    """Return a set of common words between two lists of words."""
    set1 = set(word.lower() for word in list1)
    set2 = set(word.lower() for word in list2)
    return set1.intersection(set2)


def main():
    s1 = input("Enter the first sentence: ")
    s2 = input("Enter the second sentence: ")

    words_s1 = s1.split()
    words_s2 = s2.split()

    print("Sentence 1:", s1)
    print("Sentence 2:", s2)
    print("Common words:", common_words(words_s1, words_s2))


if __name__ == "__main__":
    main()