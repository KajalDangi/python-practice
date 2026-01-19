"""
Practice 8: Copy File Content
Task:
- Copy source.txt to backup.txt
"""

try:
    with open("source.txt") as src:
        content = src.read()
except FileNotFoundError:
    print("source.txt not found.")
else:
    with open("backup.txt", "wt") as bk:
        bk.write(content)
    print("Content copied to backup.txt")
