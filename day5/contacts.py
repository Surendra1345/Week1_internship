import json
import os

FILE="contacts.json"

def load_contacts():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)
    else:
        return []

def save_contacts(contacts):
    with open(FILE,"w") as f:
        json.dump(contacts,f,indent=4)
        print("Contacts saved successfully.")

def add_contact():
    name=input("Enter the name:")
    phone=input("Enter the phone number:")
    email=input("Enter the email:")

    contacts=load_contacts()
    for c in contacts:
        if c["name"].lower()==name.lower():
            print("Contact already exists.")
            return
    contacts.append({
            "name":name,
            "phone":phone,
            "email":email
           })
    save_contacts(contacts)
    print("Contact added successfully.")

def list_contacts():
    contacts=load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for i,contact in enumerate(contacts,1):
        print(str(i)+" ."+contact["name"])
        print("Phone:"+contact["phone"])
        print("Email:"+contact["email"])
        print()
    print("Total :"+str(len(contacts))+" contacts")

def search_contact():
    name=input("Enter the name to search:")
    contacts=load_contacts()
    for c in contacts:
        if c["name"].lower()==name.lower():
            print("Contact found:")
            print("Name:"+c["name"])
            print("Phone:"+c["phone"])
            print("Email:"+c["email"])
            return
    print("Contact not found.")
    print("Total :"+str(len(contacts))+" contacts")

def update_contact():
    name=input("Enter the name to update:")
    contacts=load_contacts()
    for c in contacts:
        if c["name"].lower()==name.lower():
            phone=input("Enter the new phone number:")
            email=input("Enter the new email:")
            c["phone"]=phone
            c["email"]=email
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")
    print("Total :"+str(len(contacts))+" contacts")

def delete_contact():
    name=input("Enter the name to delete:")
    contacts=load_contacts()
    for c in contacts:
        if c["name"].lower()==name.lower():
            contacts.remove(c)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")
    print("Total :"+str(len(contacts))+" contacts")

def show_stats():
    contacts=load_contacts()
    print("Total contacts:"+str(len(contacts)))
    if contacts:
        print("Contacts:")
        for c in contacts:
            print("Name:"+c["name"])
            print("Phone:"+c["phone"])
            print("Email:"+c["email"])
            print()

def main():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Show Stats")
        print("7. Exit")

        choice=input("Enter your choice:")
        if choice=="1":
            add_contact()
        elif choice=="2":
            list_contacts()
        elif choice=="3":
            search_contact()
        elif choice=="4":
            update_contact()
        elif choice=="5":
            delete_contact()
        elif choice=="6":
            show_stats()
        elif choice=="7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()
