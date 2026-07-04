phone_book = {}
while True:
    print("Phone menu: ")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. Display all contacts")
    print("5. Exit")
    cho = input("Enter your choice (1-5): ")
    if cho == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        phone_book[name] = number
        print(f"Contact {name} added successfully.")
    elif cho == '2':
        name = input("Enter contact name to search: ")
        if name in phone_book:
            print(f"Contact found: {name} - {phone_book[name]}")
        else:
            print(f"Contact {name} not found.")
    elif cho =='3':
        name = input("Enter contact name to delete: ")
        if name in phone_book:
            del phone_book[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")
    elif cho =='4':
        print("All Contacts:")
        for name , number in phone_book.items():
            print(f"{name} - {number}")
    elif cho =='5':
        print("Exiting the phone book application.")
        break