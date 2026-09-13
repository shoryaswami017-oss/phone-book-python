import json
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(phone_book, file, indent=4)
phone_book = load_contacts()


def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")

    phone_book[name] = number
    save_contacts()

    print(f"Contact {name} added successfully.")

def search_contact():
    name = input("Enter contact name to search: ")

    if name in phone_book:
        print(f"Contact found: {name} - {phone_book[name]}")
    else:
        print(f"Contact {name} not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in phone_book:
        del phone_book[name]
        save_contacts()
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")


def display_contacts():
    if not phone_book:
        print("Phone book is empty.")
        return

    print("All Contacts:")

    for name, number in phone_book.items():
        print(f"{name} - {number}")


while True:
    print("\nPhone Book Menu:")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        display_contacts()

    elif choice == "5":
        print("Exiting the phone book application.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
