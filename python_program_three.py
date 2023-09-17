import os

contacts = []

def add_contact():
    name = input("Enter the name of the contact: ").strip()
    phone = input("Enter the phone number of the contact: ").strip()
    email = input("Enter the email address of the contact: ").strip()

    # Check if the contact name already exists
    for contact in contacts:
        if contact['name'] == name:
            print(f"A contact with the name '{name}' already exists.")
            return

    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        print("List of Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    name = input("Enter the name to search for: ").strip()
    found = False
    for contact in contacts:
        if contact['name'] == name:
            print("Contact Details:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
            break
    if not found:
        print(f"Contact with name '{name}' not found.")

def save_contacts_to_file():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}\n")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Save Contacts to File")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            save_contacts_to_file()
            print("Contacts saved to 'contacts.txt'.")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()
