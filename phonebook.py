contacts = []

def show_menu():
    print("\n=== Phone Book ===")
    print("1. Add contact")
    print("2. Show all contacts")
    print("3. Search contact")
    print("4. Exit")

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print("Contact added successfully!")

def show_contacts():
    if len(contacts) == 0:
        print("No contacts yet.")
    else:
        print("--- All Contacts ---")
        for contact in contacts:
            print(f"{contact['name']}: {contact['phone']}")

def search_contact():
    search_name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f"Found: {contact['name']} - {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

# --- Main Loop ---
while True:
    show_menu()
    choice = input("Choose (1-4): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")