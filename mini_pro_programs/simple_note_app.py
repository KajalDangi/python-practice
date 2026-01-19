"""
Practice 7: Simple Notes App
Menu:
1. Write note
2. View notes
3. Exit
"""

def show_menu():
    print("\n_____________________________")
    print("     SIMPLE NOTES APP")
    print("_____________________________")
    print("1 : WRITE NOTE")
    print("2 : VIEW NOTES")
    print("3 : EXIT")
    print("_____________________________")

def write_note(note):
    with open("Notes.txt", "a") as fh:
        fh.write(note + "\n")
    print("Note saved successfully.")

def view_notes():
    try:
        with open("Notes.txt", "r") as fh:
            empty = True
            for line in fh:
                print(line.rstrip("\n"))
                empty = False
            if empty:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes file found. Write a note first.")

while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        note = input("Write your note:\n")
        write_note(note)

    elif choice == 2:
        view_notes()

    elif choice == 3:
        print("Exiting... Thank you!")
        break

    else:
        print("Please choose a valid option (1–3).")