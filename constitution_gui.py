#
"""
frames = left frame for tree, midlle display, right frame for input search
"""

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import numpy


constitution = []



class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Bangladesh Constitution")
        self.geometry("680x500")
        self.resizable(False, False)

        self.create_frame()


    def create_frame(self):
        treeframe = tk.Frame(self, height=500, width=160)
        treeframe.place(x=0,y=0)
        #treeview
        treeview = ttk.Treeview(treeframe, column='sections', show='tree', height=500)
        treeview.heading('sections', text='sections')
        treeview.insert(parent='', index='end', iid=0, text='Part One', open=False)
        treeview.insert(parent='', index='end', iid=1, text='Part Two', open=False)
        treeview.insert(parent='', index='end', iid=2, text='Part Three', open=False)
        treeview.insert(parent='', index='end', iid=3, text='Part Four', open=False)
        treeview.insert(parent='', index='end', iid=4, text='Part Five', open=False)
        treeview.insert(parent='', index='end', iid=5, text='Part Six', open=False)
        treeview.insert(parent='', index='end', iid=6, text='Part Seven', open=False)
        treeview.insert(parent='', index='end', iid=7, text='Part Eight', open=False)
        treeview.insert(parent='', index='end', iid=8, text='Part Nine', open=False)
        treeview.insert(parent='', index='end', iid=9, text='Part Ten', open=False)
        treeview.insert(parent='', index='end', iid=10, text='Part Eleven', open=False)

        #subsections
        treeview.insert(parent='', index='end', iid=401, text='Chapter One', open=False)
        treeview.insert(parent='', index='end', iid=402, text='Chapter Two', open=False)
        treeview.insert(parent='', index='end', iid=403, text='Chapter Three', open=False)
        treeview.insert(parent='', index='end', iid=404, text='Chapter Four', open=False)
        treeview.insert(parent='', index='end', iid=405, text='Chapter Five', open=False)

        treeview.insert(parent='', index='end', iid=501, text='Chapter One', open=False)
        treeview.insert(parent='', index='end', iid=502, text='Chapter Two', open=False)
        treeview.insert(parent='', index='end', iid=503, text='Chapter Three', open=False)

        treeview.insert(parent='', index='end', iid=601, text='Chapter One', open=False)
        treeview.insert(parent='', index='end', iid=602, text='Chapter Two', open=False)
        treeview.insert(parent='', index='end', iid=603, text='Chapter Three', open=False)

        treeview.insert(parent='', index='end', iid=901, text='Chapter One', open=False)
        treeview.insert(parent='', index='end', iid=902, text='Chapter Two', open=False)
        treeview.insert(parent='', index='end', iid=903, text='Part Nine(A)', open=False)



        #moving to subsections
        treeview.move(item=401, parent=3, index=0)
        treeview.move(item=402, parent=3, index=1)
        treeview.move(item=403, parent=3, index=2)
        treeview.move(item=404, parent=3, index=3)
        treeview.move(item=405, parent=3, index=4)

        treeview.move(item=501, parent=4, index=0)
        treeview.move(item=502, parent=4, index=1)
        treeview.move(item=503, parent=4, index=2)

        treeview.move(item=601, parent=5, index=0)
        treeview.move(item=602, parent=5, index=1)
        treeview.move(item=603, parent=5, index=2)

        treeview.move(item=901, parent=8, index=0)
        treeview.move(item=902, parent=8, index=1)
        treeview.move(item=903, parent=8, index=2)


        treeview.place(x=0, y=0)



        #Display Frame
        displayframe = tk.Frame(self, height=500, width=400)

       #title frame
        title_frame=tk.Frame(displayframe, height=50, width=400)
        title = ttk.Label(title_frame, text="This is Article Title")
        title.place(x=100, y=10)
        title_frame.place(x=0, y=0)

        #article Content
        content_frame = tk.Frame(displayframe, height=450, width=400)
        content_frame_label= tk.Label(content_frame, text="Lorem ipsum dolor sit amet, consectetur Lorem ipsum dolor sit amet, consecteturLorem ipsum dolor sit amet, consectetur", wraplength=400, justify='left')
        content_frame_label.place(x=0, y=20)
        content_frame.place(x=0, y=51)

        displayframe.place(x=160, y=0)

        def find():

            get_find = find_var.get()
            if get_find:
                label = tk.Label(displayframe, text=get_find +' is searching')
                label.pack()


        buttonframe = tk.Frame(self, height=500, width=120, bg='green')


        find_var = tk.StringVar()
        find_btn = ttk.Button(buttonframe, text='Find', command=find)
        find_btn.place(x=30,y=80)
        find_label_entry = ttk.Entry(buttonframe, width=80, textvariable=find_var)
        find_label_entry.place(x=0, y=50)
        buttonframe.place(x=560, y=0)



if __name__ == "__main__":
    app= App()
    app.mainloop()