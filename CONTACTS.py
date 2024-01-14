class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, contact):
        if contact.name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[contact.name] = contact
            print("Contact added successfully.")
    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact removed successfully.")
        else:
            print("Contact does not exist.")
    def find_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("Contact does not exist.")
    def list_contacts(self):
        print("\nContact List:")
        for contact in self.contacts.values():
            print(f"Name: {contact.name}, Phone: {contact.phone}")
if __name__ == "__main__":
    contact_book = ContactBook()
    while True:
        print("\n1. Add Contact")
        print("2. Remove Contact")
        print("3. Find Contact")
        print("4. List Contacts")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contact = Contact(name, phone)
            contact_book.add_contact(contact)
        elif choice == 2:
            name = input("Enter name: ")
            contact_book.remove_contact(name)
        elif choice == 3:
            name = input("Enter name: ")
            contact_book.find_contact(name)
        elif choice == 4:
            contact_book.list_contacts()
        elif choice == 5:
            break
        else:
            print("Invalid choice.")