"""
Practice 4: Student Marks File
Task:
- Ask student name and marks
- Save as Name : Marks
- Display all records
"""

def write_records(records):
    with open("student_record.txt", "at") as fh:
        for name in records:
            fh.write(f"{name} : {records[name]}\n")

def read_records():
    with open("student_record.txt") as fh:
        for line in fh:
            print(line.rstrip("\n"))

records = {}

while True:
    try:
        n = int(input("Enter number of students: "))
        break
    except ValueError:
        print("Invalid input.")

for i in range(1, n + 1):
    name = input(f"Enter name of student {i}: ")
    while True:
        try:
            marks = int(input("Enter marks: "))
            break
        except ValueError:
            print("Marks must be integer.")
    records[name] = marks

write_records(records)
read_records()
