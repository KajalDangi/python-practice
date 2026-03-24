"""
Program: Set Intersection

Description:
This program demonstrates how to compute the intersection of two sets.
The intersection contains only the elements that are present in both sets.
"""

def set_intersection(set1, set2):
    """Return the intersection of two sets."""
    return set1.intersection(set2)


def main():
    set1 = {1, 2, 3, 45, 67}
    set2 = {3, 4, 5, 6, 7, 8}

    result = set_intersection(set1, set2)

    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Intersection:", result)


if __name__ == "__main__":
    main()