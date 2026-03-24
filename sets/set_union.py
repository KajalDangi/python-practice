"""
Program: Set Union
"""

def set_union(set1, set2):
    """Return the union of two sets."""
    return set1.union(set2)


def main():
    set1 = {1, 2, 3, 45, 67}
    set2 = {3, 4, 5, 6, 7, 8}

    result = set_union(set1, set2)

    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Union:", result)


if __name__ == "__main__":
    main()