"""Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
marks={"Alice":85,"John":96,"Jack":56,"Smith":78}

student_name=input("Enter the student's name: ")
if student_name in marks:
    print(f"{student_name}'s marks:{marks[student_name]}")
else:
    print("Student not found")

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