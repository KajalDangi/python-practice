"""
Practice 5: File Exists Check
Task:
- If file exists → read
- Else → create and write message
"""

file_name = input("Enter file name: ")

try:
    with open(file_name) as fh:
        print("\nFile exists. Reading content:")
        for line in fh:
            print(line.rstrip("\n"))
except FileNotFoundError:
    with open(file_name, "xt") as fh:
        fh.write("New file created.")
    print("File did not exist. New file created.")
