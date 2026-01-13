
"""
Task 1: Read a File and Handle Errors
"""

file_name = "sample.txt"

try:
    with open(file_name, "r") as fh:
        for line in fh:
            print(line.rstrip("\n"))

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
