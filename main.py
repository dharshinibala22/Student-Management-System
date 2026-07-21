import tkinter as tk

window = tk.Tk()
window.title("Student Management System")
window.geometry("800x500")

label = tk.Label(window, text="Student Management System", font=("Arial", 20))
label.pack(pady=20)

window.mainloop()