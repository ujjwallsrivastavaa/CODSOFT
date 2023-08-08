import tkinter as tk
from tkinter import messagebox
import random
import string
root = tk.Tk()
root.title("Password Generator")
def generate_password():
    password_length = int(entry_length.get())
    if password_length < 8:
        messagebox.showerror("Error", "Password length must be at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    lbl_password.config(text="Generated Password: " + password)
label_length = tk.Label(root, text="Enter password length: ")
label_length.pack(pady=10)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.pack(pady=10)

lbl_password = tk.Label(root, text="")
lbl_password.pack(pady=10)
root.mainloop()