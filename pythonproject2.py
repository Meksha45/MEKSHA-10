import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def mark_done():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, f"✔️ {task}")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

# Set up the main window
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("450x500")
root.configure(bg="#2C2F33")
root.resizable(False, False)

# Header Label
header = tk.Label(root, text="My To-Do List", font=("Arial", 20, "bold"), bg="#2C2F33", fg="#FFFFFF")
header.pack(pady=15)

# Entry field
entry = tk.Entry(root, width=28, font=('Arial', 14), bg="#40444B", fg="white", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#7289DA")
entry.pack(pady=10)

# Buttons
btn_style = {"width": 15, "font": ("Arial", 12), "bg": "#7289DA", "fg": "white", "bd": 0, "activebackground": "#5b6eae"}

add_btn = tk.Button(root, text="Add Task", command=add_task, **btn_style)
add_btn.pack(pady=5)

remove_btn = tk.Button(root, text="Remove Task", command=remove_task, **btn_style)
remove_btn.pack(pady=5)

done_btn = tk.Button(root, text="Mark as Done", command=mark_done, **btn_style)
done_btn.pack(pady=5)

# Task List
listbox = tk.Listbox(root, width=40, height=10, font=('Arial', 12), bg="#23272A", fg="white", selectbackground="#7289DA", bd=0, highlightthickness=0)
listbox.pack(pady=15)

# Run the app
root.mainloop()
