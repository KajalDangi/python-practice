def find_unique_elements(lst):
    freq = {}
    unique_elements = []

    for num in lst:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count == 1:
            unique_elements.append(num)

    return unique_elements


def main():
    original_list = [1, 2, 3, 3, 4, 6, 3, 2]

    print("Original list:", original_list)
    print("Unique elements:", find_unique_elements(original_list))


if __name__ == "__main__":
    main()