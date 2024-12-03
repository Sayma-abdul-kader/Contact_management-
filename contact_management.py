import os
import csv

class ContactBook:
    def __init__(self, filename="contacts.csv"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def add_contact(self, name, phone, email, address):
        if any(contact['Phone'] == phone for contact in self.contacts):
            print("Error: Duplicate phone number not allowed.")
            return

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        print("\nContacts:")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")

    def save_contacts(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email", "Address"])
            writer.writeheader()
            writer.writerows(self.contacts)

    def load_contacts(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, mode="r") as file:
            reader = csv.DictReader(file)
            self.contacts = [row for row in reader]

    def remove_contact(self, phone):
        for contact in self.contacts:
            if contact['Phone'] == phone:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact removed successfully.")
                return

        print("Error: Contact not found.")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]

        if not results:
            print("No matching contacts found.")
            return

        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")


def display_menu():
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")


def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            if not phone.isdigit():
                print("Error: Phone number must be numeric.")
                continue

            email = input("Enter Email: ")
            address = input("Enter Address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            phone = input("Enter the phone number of the contact to remove: ")
            contact_book.remove_contact(phone)

        elif choice == "4":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
