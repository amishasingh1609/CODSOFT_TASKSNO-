contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            for name, details in contacts.items():
                print(name, "-", details["phone"])

    elif choice == "3":
        search = input("Enter name or phone number: ")

        for name, details in contacts.items():
            if search.lower() in name.lower() or search in details["phone"]:
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("Address:", details["address"])

    elif choice == "4":
        name = input("Enter contact name to update: ")

        if name in contacts:
            contacts[name]["phone"] = input("Enter new phone: ")
            contacts[name]["email"] = input("Enter new email: ")
            contacts[name]["address"] = input("Enter new address: ")
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")