"""
Program: Symmetric Difference

Description:
This program computes the symmetric difference between two sets.
The result contains elements that exist in either set but not in both.
Symmetric difference is commutative: A △ B = B △ A.
"""

def symmetric_difference(set1, set2):
    """Return elements present in either set1 or set2 but not both."""
    return set1.symmetric_difference(set2)


def main():
    set1 = {1, 2, 3, 45, 67}
    set2 = {3, 4, 5, 6, 7, 8}

    result = symmetric_difference(set1, set2)

    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Symmetric Difference:", result)


if __name__ == "__main__":
    main()