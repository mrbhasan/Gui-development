import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.geometry("500x450+500+200")
root.resizable(False, False)
root.config(bg='#8486ff')


#a list frame for containing the list
list_frame = tk.Frame(root)
list_frame.pack(pady=20)

listbox = tk.Listbox(list_frame, width=30, height=10, bd=0, fg="#9b9ca9",
                     font=('calibri 14'))
listbox.pack(side='left')

task_list = []

for item in task_list:
    listbox.insert(tk.END, item)


#adding a scrollbar to the listbox
list_scrollbar = tk.Scrollbar(list_frame)
list_scrollbar.pack(side='right', fill='both')
listbox.config(yscrollcommand=list_scrollbar.set)
list_scrollbar.config(command=listbox.yview)


#Entrybox
task_entry = tk.Entry(root, width=25, bd=0, font=('calibri 16'))
task_entry.pack(pady=20)


#buttonframe for containing all the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

#adding button to button frame
add_task_btn = tk.Button(
    button_frame,
    text='Add Task',
    font=('Calibri 13'),
    padx=10,
    pady=10,
    bg='#58a342',
    bd=0,
    fg='#ffffff')
add_task_btn.pack(side='left', fill='both')

remove_task_btn = tk.Button(
    button_frame,
    text='Remove Task',
    font=('Calibri 13'),
    padx=10,
    pady=10,
    bg='#a34842',
    bd=0,
    fg='#ffffff')
remove_task_btn.pack(side='left', fill='both')


#functions for handling button
def add_task():
    new_task = task_entry.get()
    if new_task != '':
        listbox.insert('end', new_task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("# WARNING", "Please Enter a task")


def remove_task():
    listbox.delete(tk.ANCHOR)


#connecting functions to button
add_task_btn.config(command=add_task)
remove_task_btn.config(command=remove_task)


root.mainloop()
