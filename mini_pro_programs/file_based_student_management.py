"""
Practice 10: File-Based Student Record System
"""

def save_data(filename, data):
    with open(filename, "at") as fh:
        for name in data:
            fh.write(f"{name} : {data[name]}\n")

def display_data(filename):
    try:
        empty = True
        with open(filename) as fh:
            for line in fh:
                print(line.rstrip("\n"))
                empty = False
            if empty:
                print("File is empty.")
    except FileNotFoundError:
        print("File does not exist.")

file_name = input("Enter file name: ")

while True:
    try:
        n = int(input("Enter number of students: "))
        break
    except ValueError:
        print("Invalid input.")

records = {}

for i in range(1, n + 1):
    name = input(f"Enter name of student {i}: ")
    while True:
        try:
            marks = int(input("Enter marks: "))
            break
        except ValueError:
            print("Invalid marks.")
    records[name] = marks

save_data(file_name, records)
display_data(file_name)
