"""
Program: Merge Two Dictionaries

"""

def merge_dicts(d1, d2):

    return d1 | d2


def main():
    dict1 = {"alex": 23, "box": 21}
    dict2 = {"ram": 11, "riya": 1}

    print(merge_dicts(dict1, dict2))


if __name__ == "__main__":
    main()
