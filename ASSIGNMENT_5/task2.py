"""Task 2: Demonstrate List Slicing
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""
numbers=[1,2,3,4,5,6,7,8,9,10]
print(f"Original list:{numbers}")
extracted_val=numbers[:5]
print(f"Extracted first five elements:{extracted_val}")
extracted_val.reverse()
print(f"Reversed extracted elements:{extracted_val}")