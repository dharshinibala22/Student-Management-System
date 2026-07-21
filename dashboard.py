import tkinter as tk

window = tk.Tk()
window.title("Dashboard")
window.geometry("900x600")
window.configure(bg="lightblue")

title = tk.Label(
    window,
    text="Student Management System Dashboard",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title.pack(pady=20)

btn_add = tk.Button(window, text="Add Student", width=20, height=2)
btn_add.pack(pady=10)

btn_view = tk.Button(window, text="View Students", width=20, height=2)
btn_view.pack(pady=10)

btn_search = tk.Button(window, text="Search Student", width=20, height=2)
btn_search.pack(pady=10)

btn_update = tk.Button(window, text="Update Student", width=20, height=2)
btn_update.pack(pady=10)

btn_delete = tk.Button(window, text="Delete Student", width=20, height=2)
btn_delete.pack(pady=10)

window.mainloop()