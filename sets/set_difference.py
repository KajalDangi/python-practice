"""
Program: Set Difference

Description:
This program computes the difference between two sets.
The result contains elements that exist in set1 but not in set2.
Note: Set difference is not symmetric.
"""

def set_difference(set1, set2):
    """Return elements present in set1 but not in set2."""
    return set1 - set2


def main():
    set1 = {1, 2, 3, 45, 67}
    set2 = {3, 4, 5, 6, 7, 8}

    result = set_difference(set1, set2)

    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Set1 - Set2:", result)


if __name__ == "__main__":
    main()