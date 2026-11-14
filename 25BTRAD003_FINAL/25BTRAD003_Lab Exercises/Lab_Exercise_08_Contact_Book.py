contacts = []
while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    choice = input("Choice: ")
    if choice == "1":
        contacts.append({"name": input("Name: "), "phone": input("Phone: "), "email": input("Email: ")})
    elif choice == "2":
        name = input("Name to search: ").lower()
        found = [c for c in contacts if c["name"].lower() == name]
        print(found if found else "Contact not found")
    elif choice == "3":
        name = input("Name to update: ").lower()
        c = next((x for x in contacts if x["name"].lower() == name), None)
        if c:
            c["phone"] = input("New phone: "); c["email"] = input("New email: ")
        else: print("Contact not found")
    elif choice == "4":
        name = input("Name to delete: ").lower()
        c = next((x for x in contacts if x["name"].lower() == name), None)
        if c: contacts.remove(c)
        else: print("Contact not found")
    elif choice == "5":
        for c in contacts: print(c)
    elif choice == "6": break
    else: print("Invalid choice")
