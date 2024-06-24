import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Contact management functions
contacts = []

def save_contacts():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file)

def load_contacts():
    global contacts
    try:
        with open('contacts.json', 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

def add_contact(name, phone, email, address):
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts()
    update_contact_list()

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def view_contact(event):
    selected_index = contact_list.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        messagebox.showinfo("Contact Details", f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")

def search_contact(query):
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    contact_list.delete(0, tk.END)
    for contact in results:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact(name, phone, email, address, index):
    contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
    save_contacts()
    update_contact_list()

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        del contacts[selected_index[0]]
        save_contacts()
        update_contact_list()

def on_add():
    name = simpledialog.askstring("Input", "Enter name:")
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email:")
    address = simpledialog.askstring("Input", "Enter address:")
    if name and phone and email and address:
        add_contact(name, phone, email, address)
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def on_update():
    selected_index = contact_list.curselection()
    if selected_index:
        contact = contacts[selected_index[0]]
        name = simpledialog.askstring("Input", "Enter name:", initialvalue=contact['name'])
        phone = simpledialog.askstring("Input", "Enter phone number:", initialvalue=contact['phone'])
        email = simpledialog.askstring("Input", "Enter email:", initialvalue=contact['email'])
        address = simpledialog.askstring("Input", "Enter address:", initialvalue=contact['address'])
        if name and phone and email and address:
            update_contact(name, phone, email, address, selected_index[0])
        else:
            messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showwarning("Selection Error", "No contact selected!")

def on_search():
    query = simpledialog.askstring("Search", "Enter name or phone number to search:")
    if query:
        search_contact(query)

# Load contacts from file
load_contacts()

# Create main application window
app = tk.Tk()
app.title("Contact Manager")

# Create and place widgets
add_button = tk.Button(app, text="Add Contact", command=on_add)
add_button.pack(pady=5)

update_button = tk.Button(app, text="Update Contact", command=on_update)
update_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=5)

search_button = tk.Button(app, text="Search Contact", command=on_search)
search_button.pack(pady=5)

contact_list = tk.Listbox(app)
contact_list.pack(pady=10, fill=tk.BOTH, expand=True)
contact_list.bind('<Double-1>', view_contact)

# Initial update of the contact list
update_contact_list()

# Start the application
app.mainloop()
