"""
Program: Remove Duplicates from a List Using Sets
"""

def remove_duplicates(lst):

    return list(set(lst))


def main():
    original_list = [1, 2, 3, 7, 6, 3, 2]

    print("Original list:", original_list)
    print("List without duplicates:", remove_duplicates(original_list))


if __name__ == "__main__":
    main()
