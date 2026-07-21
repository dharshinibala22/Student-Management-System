import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin123":
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

window = tk.Tk()
window.title("Login")
window.geometry("400x300")

title = tk.Label(window, text="Student Management System", font=("Arial", 16, "bold"))
title.pack(pady=20)

tk.Label(window, text="Username").pack()
username_entry = tk.Entry(window)
username_entry.pack()

tk.Label(window, text="Password").pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

tk.Button(window, text="Login", command=login).pack(pady=20)

window.mainloop()