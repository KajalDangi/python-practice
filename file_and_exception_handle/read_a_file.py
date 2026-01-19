"""
Practice 1: Read a File
Task:
- Ask user for a filename
- Read and print file line by line
- If file doesn’t exist → show friendly error
"""

file_name = input("Enter the name of the file you want to read: ")

try:
    with open(file_name) as fh:
        count = 0
        for line in fh:
            print(line.rstrip("\n"))
            count += 1
        if count == 0:
            print("File is empty.")
except FileNotFoundError:
    print(f"'{file_name}' does not exist.")
