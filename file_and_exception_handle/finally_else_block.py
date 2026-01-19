"""
Practice 9: Exception with else & finally
"""

file_name = input("Enter file name: ")

try:
    with open(file_name) as fh:
        for line in fh:
            print(line.rstrip("\n"))
except FileNotFoundError:
    print("File not found.")
finally:
    print("Operation completed.")
