
import tkinter as tk
from tkinter import messagebox

tasks = []
FILE_NAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        pass


def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    tasks.append(task)
    save_tasks()
    task_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Task added successfully!")


def view_tasks():
    task_list.delete(0, tk.END)

    if len(tasks) == 0:
        task_list.insert(tk.END, "No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            task_list.insert(tk.END, str(i) + ". " + task)

    task_list.pack(padx=20, pady=15)


def remove_task():
    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Click View Tasks and select a task first!"
        )
        return

    number = selected[0]

    if number >= len(tasks):
        return

    removed_task = tasks.pop(number)
    save_tasks()

    task_list.delete(0, tk.END)

    for i, task in enumerate(tasks, start=1):
        task_list.insert(tk.END, str(i) + ". " + task)

    messagebox.showinfo("Success", "Task removed: " + removed_task)


root = tk.Tk()
root.title("My To-Do List")
root.geometry("520x600")
root.configure(bg="#eaf2f8")
root.resizable(False, False)

title = tk.Label(
    root,
    text="MY TO-DO LIST",
    font=("Arial", 24, "bold"),
    bg="#eaf2f8",
    fg="#2c3e50"
)
title.pack(pady=(25, 5))

subtitle = tk.Label(
    root,
    text="Organize your daily tasks",
    font=("Arial", 11),
    bg="#eaf2f8",
    fg="#7f8c8d"
)
subtitle.pack(pady=5)

task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=32,
    bd=2
)
task_entry.pack(pady=20, ipady=7)

button_frame = tk.Frame(root, bg="#eaf2f8")
button_frame.pack(pady=5)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    font=("Arial", 11, "bold"),
    bg="#3498db",
    fg="white",
    width=12,
    command=add_task
)
add_button.pack(side="left", padx=5)

view_button = tk.Button(
    button_frame,
    text="View Tasks",
    font=("Arial", 11, "bold"),
    bg="#2ecc71",
    fg="white",
    width=12,
    command=view_tasks
)
view_button.pack(side="left", padx=5)

remove_button = tk.Button(
    button_frame,
    text="Remove Task",
    font=("Arial", 11, "bold"),
    bg="#e74c3c",
    fg="white",
    width=12,
    command=remove_task
)
remove_button.pack(side="left", padx=5)

task_list = tk.Listbox(
    root,
    font=("Arial", 12),
    width=48,
    height=12,
    selectbackground="#3498db",
    bd=0
)

footer = tk.Label(
    root,
    text="Stay Organized • Complete Your Tasks",
    font=("Arial", 10),
    bg="#eaf2f8",
    fg="#7f8c8d"
)
footer.pack(side="bottom", pady=15)

load_tasks()

root.mainloop()
