import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task !")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete !")

def update_task():
    try:
        index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        if updated_task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, updated_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

root = tk.Tk()
root.title("To Do List")

entry_task = tk.Entry(root, width=50)
entry_task.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

btn_add = tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white")
btn_add.grid(row=0, column=3, padx=5, pady=5)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task, bg="red", fg="white")
btn_delete.grid(row=1, column=3, padx=5, pady=5)

btn_update = tk.Button(root, text="Update Task", command=update_task, bg="blue", fg="white")
btn_update.grid(row=2, column=3, padx=5, pady=5)

listbox_tasks = tk.Listbox(root, height=15, width=60, selectbackground="yellow")
listbox_tasks.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

root.mainloop()