import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# -----------------------------
# DATABASE
# -----------------------------
def connect_db():
    conn = sqlite3.connect("student.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        department TEXT,
        phone TEXT,
        email TEXT
    )
    """)

    conn.commit()
    return conn


# -----------------------------
# CLEAR FIELDS
# -----------------------------
def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# -----------------------------
# SAVE STUDENT
# -----------------------------
def save_student():

    if name_entry.get().strip() == "":
        messagebox.showerror("Error", "Name is required!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students
    (name, age, gender, department, phone, email)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name_entry.get(),
        age_entry.get(),
        gender_entry.get(),
        dept_entry.get(),
        phone_entry.get(),
        email_entry.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Success",
        "Student Added Successfully!"
    )

    clear_fields()


# -----------------------------
# VIEW STUDENTS
# -----------------------------
def view_students():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    view = tk.Toplevel(window)
    view.title("All Students")
    view.geometry("900x400")

    tree = ttk.Treeview(view)

    tree["columns"] = (
        "ID",
        "Name",
        "Age",
        "Gender",
        "Department",
        "Phone",
        "Email"
    )

    tree.column("#0", width=0, stretch=tk.NO)

    for col in tree["columns"]:
        tree.column(col, width=120)
        tree.heading(col, text=col)

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(fill="both", expand=True)


# -----------------------------
# SEARCH STUDENT
# -----------------------------
def search_students():

    keyword = name_entry.get().strip()

    if keyword == "":
        messagebox.showwarning(
            "Warning",
            "Enter a student name to search."
        )
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + keyword + '%',)
    )

    rows = cursor.fetchall()

    conn.close()

    result = tk.Toplevel(window)
    result.title("Search Results")
    result.geometry("900x400")

    tree = ttk.Treeview(result)

    tree["columns"] = (
        "ID",
        "Name",
        "Age",
        "Gender",
        "Department",
        "Phone",
        "Email"
    )

    tree.column("#0", width=0, stretch=tk.NO)

    for col in tree["columns"]:
        tree.column(col, width=120)
        tree.heading(col, text=col)

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(fill="both", expand=True)

    if len(rows) == 0:
        messagebox.showinfo(
            "Search",
            "No student found."
        )


# -----------------------------
# UPDATE STUDENT
# -----------------------------
def update_student():

    update_window = tk.Toplevel(window)
    update_window.title("Update Student")
    update_window.geometry("400x450")

    tk.Label(update_window, text="Student ID").pack(pady=3)
    id_entry = tk.Entry(update_window)
    id_entry.pack()

    tk.Label(update_window, text="Name").pack(pady=3)
    name = tk.Entry(update_window)
    name.pack()

    tk.Label(update_window, text="Age").pack(pady=3)
    age = tk.Entry(update_window)
    age.pack()

    tk.Label(update_window, text="Gender").pack(pady=3)
    gender = tk.Entry(update_window)
    gender.pack()

    tk.Label(update_window, text="Department").pack(pady=3)
    department = tk.Entry(update_window)
    department.pack()

    tk.Label(update_window, text="Phone").pack(pady=3)
    phone = tk.Entry(update_window)
    phone.pack()

    tk.Label(update_window, text="Email").pack(pady=3)
    email = tk.Entry(update_window)
    email.pack()

    def update():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE students
        SET name=?, age=?, gender=?, department=?, phone=?, email=?
        WHERE id=?
        """, (
            name.get(),
            age.get(),
            gender.get(),
            department.get(),
            phone.get(),
            email.get(),
            id_entry.get()
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Student Updated Successfully!"
        )

        update_window.destroy()

    tk.Button(
        update_window,
        text="Update",
        command=update,
        bg="green",
        fg="white",
        width=15
    ).pack(pady=15)


# -----------------------------
# DELETE STUDENT
# -----------------------------
def delete_student():

    delete_window = tk.Toplevel(window)
    delete_window.title("Delete Student")
    delete_window.geometry("350x180")

    tk.Label(
        delete_window,
        text="Enter Student ID"
    ).pack(pady=10)

    id_entry = tk.Entry(delete_window)
    id_entry.pack()

    def delete():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id=?",
            (id_entry.get(),)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            "Student Deleted Successfully!"
        )

        delete_window.destroy()

    tk.Button(
        delete_window,
        text="Delete",
        command=delete,
        bg="red",
        fg="white",
        width=15
    ).pack(pady=20)


# -----------------------------
# MAIN WINDOW
# -----------------------------
window = tk.Tk()
window.title("Student Management System")
window.geometry("500x650")
window.resizable(False, False)

tk.Label(
    window,
    text="Student Management System",
    font=("Arial", 18, "bold")
).pack(pady=10)

# Name
tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window, width=40)
name_entry.pack(pady=5)

# Age
tk.Label(window, text="Age").pack()
age_entry = tk.Entry(window, width=40)
age_entry.pack(pady=5)

# Gender
tk.Label(window, text="Gender").pack()
gender_entry = tk.Entry(window, width=40)
gender_entry.pack(pady=5)

# Department
tk.Label(window, text="Department").pack()
dept_entry = tk.Entry(window, width=40)
dept_entry.pack(pady=5)

# Phone
tk.Label(window, text="Phone").pack()
phone_entry = tk.Entry(window, width=40)
phone_entry.pack(pady=5)

# Email
tk.Label(window, text="Email").pack()
email_entry = tk.Entry(window, width=40)
email_entry.pack(pady=5)

# Buttons
tk.Button(
    window,
    text="Save Student",
    command=save_student,
    width=20,
    bg="green",
    fg="white"
).pack(pady=5)

tk.Button(
    window,
    text="View Students",
    command=view_students,
    width=20,
    bg="blue",
    fg="white"
).pack(pady=5)

tk.Button(
    window,
    text="Search Student",
    command=search_students,
    width=20,
    bg="orange",
    fg="white"
).pack(pady=5)

tk.Button(
    window,
    text="Update Student",
    command=update_student,
    width=20,
    bg="purple",
    fg="white"
).pack(pady=5)

tk.Button(
    window,
    text="Delete Student",
    command=delete_student,
    width=20,
    bg="red",
    fg="white"
).pack(pady=5)

tk.Button(
    window,
    text="Clear Fields",
    command=clear_fields,
    width=20
).pack(pady=5)

# Create database/table
connect_db()

window.mainloop()