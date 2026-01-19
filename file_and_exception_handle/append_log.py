"""
Practice 3: Append Logs
Task:
- Append user message to log.txt
- Display full log
"""

message = input("Enter a log message: ")

with open("log.txt", "at") as fh:
    fh.write(message + "\n")

print("\nLog File Content:")
with open("log.txt") as fh:
    for line in fh:
        print(line.rstrip("\n"))
