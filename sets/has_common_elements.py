def has_common_elements(list1, list2):
    """Return True if two lists share at least one common element."""
    return not set(list1).isdisjoint(list2)


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = [1]

    print(has_common_elements(list1, list2))


if __name__ == "__main__":
    main()