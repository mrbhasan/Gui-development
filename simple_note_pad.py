import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import tkinter.filedialog as fd
import os 


w = tk.Tk()
w.title("Simple Notepad")
w.geometry('500x400+300+200')
w.resizable(False, False)

#Frames
text_frame = tk.Frame(w, height=500, width=400)
text_frame.grid(row=0, column=1)

button_frame = tk.Frame(w, height=500, width=130, bg='#082283')
button_frame.grid(row=0, column=0)

#adding button to frames
new_note_btn = tk.Button(button_frame, text='New Note',
                         bg='#b6e6d9', fg='#515058', width=10, bd=0)
new_note_btn.place(x=10, y=10)


oepn_note_btn = tk.Button(
    button_frame, text='Open Note', bg='#b6e6d9', fg='#515058', width=10, bd=0)
oepn_note_btn.place(x=10, y=50)


#functions

#this button will be used to define new note
def new_note():
    textbox = tk.Text(text_frame, width=43, height=15)
    textbox.place(x=10, y=20)
    
    save_button = tk.Button(text_frame, text='Save')
    save_button.place(x=20, y=300)
    

    close_button = tk.Button(text_frame, text='close')
    close_button.place(x=300, y=290)
    
    def save():
        save_data = textbox.get(1.0, tk.END)
        file = fd.asksaveasfilename(
            initialfile='Untitled.txt',
            defaultextension='.txt',
            filetypes=[
                ('All Files', '.*'),
                ('Text Documents', '.txt')
            ]
        )
        filev2 = open(file, 'w')
        filev2.write(save_data)
        filev2.close()

    def close():
        textbox.destroy()
        save_button.destroy()
        close_button.destroy()

    save_button.config(command=save)
    close_button.config(command=close)



#open note function with edit functionality
def open_note():
    file = fd.askopenfilename()

    filev2 = open(file, 'r')
    textbox = tk.Text(text_frame, width=43, height=15)
    textbox.place(x=10, y=20)

    upate_btn = tk.Button(text_frame, text='Upate')
    upate_btn.place(x=20, y=300)
    

    close_button = tk.Button(text_frame, text='close')
    close_button.place(x=300, y=290)
    
    textbox.insert(1.0, filev2.read())
    filev2.close()

    def update():
        text_data = textbox.get(1.0, 'end')
        filev3 = open(file, 'w')
        filev3.write(text_data)
        filev3.close()

    def close():
        textbox.destroy()
        upate_btn.destroy()
        close_button.destroy()


    upate_btn.config(command=update)
    close_button.config(command=close)



#connecting button with functions
new_note_btn.config(command=new_note)
oepn_note_btn.config(command=open_note)

w.mainloop()
