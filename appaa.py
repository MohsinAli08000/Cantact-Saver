# Simple Contact Manager App

# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add a new contact
def add_contact(name, phone_number):
    contacts[name] = phone_number
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("List of Contacts:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
    else:
        print("No contacts found.")

# Function to search for a contact by name
def search_contact(name):
    if name in contacts:
        print(f"Contact found - {name}: {contacts[name]}")
    else:
        print("Contact not found.")

# Main function to run the application
def main():
    while True:
        print("\nSimple Contact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            add_contact(name, phone_number)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
