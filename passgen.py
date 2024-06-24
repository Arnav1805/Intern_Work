import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1 character."
    
    # Define the character set: uppercase, lowercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def on_generate():
    try:
        length = int(entry.get())
        if length < 1:
            raise ValueError
        password = generate_password(length)
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive integer for the password length.")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create and place widgets
prompt_label = tk.Label(app, text="Enter the desired length for the password:")
prompt_label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

# Start the application
app.mainloop()
