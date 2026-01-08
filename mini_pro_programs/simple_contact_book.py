""""
Simple Contact Book
Features:
- Add contact
- Search contact
- Delete contact
- View all contacts
"""

contact_book = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact_book[name] = phone
        print("Contact added.")

    elif choice == "2":
        name = input("Enter name: ")
        if name in contact_book:
            print(name, ":", contact_book[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name: ")
        if name in contact_book:
            del contact_book[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        if not contact_book:
            print("Contact book is empty.")
        else:
            for name, phone in contact_book.items():
                print(name, ":", phone)

    elif choice == "5":
        print("Exiting contact book.")
        break

    else:
        print("Invalid choice.")



