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

