"""
Practice 6: Error-Proof Input
Task:
- Ask user for marks
- Validate input
- Save to file
"""

while True:
    try:
        marks = int(input("Enter marks: "))
        break
    except ValueError:
        print("Marks must be an integer.")

with open("marks.txt", "wt") as fh:
    fh.write(str(marks))

print("Saved marks:")
with open("marks.txt") as fh:
    print(fh.read())
