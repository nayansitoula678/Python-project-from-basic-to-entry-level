
contact_list = {}

def add_contact(name, phone, email):
    if name in contact_list:
        print(f"{name} is already in the contact list.")
    else:
        contact_list[name] = {"Phone": phone, "Email": email}
        print(f"{name} has been added.")

def view_contacts():
    if not contact_list:
        print("The contact list is empty.")
    else:
        print("\nContact List:")
        for name, details in contact_list.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")


def search_contact(name):
    if name in contact_list:
        print(f"\n{name}'s Details: Phone: {contact_list[name]['Phone']}, Email: {contact_list[name]['Email']}")
    else:
        print(f"\n{name} is not in the contact list.")

def delete_contact(name):
    if name in contact_list:
        del contact_list[name]
        print(f"{name} has been deleted.")
    else:
        print(f"{name} is not in the contact list.")


while True:
    print("\n--- Contact List Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "5":
        print("Exiting Contact List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
