"""
Practice 2: Write Student Names
Task:
- Ask how many names to enter
- Write names to students.txt
- Read and display file
"""

file_name = "students.txt"

while True:
    try:
        n = int(input("Enter number of students: "))
        break
    except ValueError:
        print("Please enter a valid number.")

with open(file_name, "wt") as fh:
    for i in range(1, n + 1):
        name = input(f"Enter name of student {i}: ")
        fh.write(name + "\n")

print("\nStudents List:")
with open(file_name) as fh:
    for line in fh:
        print(line.rstrip("\n"))
