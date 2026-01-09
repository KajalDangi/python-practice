"""
Simple Contact Book
Features:
- Add contact
- Search contact
- Delete contact
- View all contacts
"""

contact_book = {}

def add_contact(name, phone):
    contact_book[name] = phone
    print("Contact added successfully.")

def search_contact(name):
    if name in contact_book:
        print(f"{name} : {contact_book[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def view_contacts():
    if not contact_book:
        print("Contact book is empty.")
    else:
        print("\nSaved Contacts:")
        for name, phone in contact_book.items():
            print(f"{name} : {phone}")

while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)

    elif choice == "2":
        name = input("Enter contact name to search: ")
        search_contact(name)

    elif choice == "3":
        name = input("Enter contact name to delete: ")
        delete_contact(name)

    elif choice == "4":
        view_contacts()

    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 to 5.")

