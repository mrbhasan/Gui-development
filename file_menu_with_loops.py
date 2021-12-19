import tkinter as tk 

#main window
root = tk.Tk()
root.geometry("500x400")
root.resizable(False, False)

#list of sub menus visibile in the submenus
File = ["New", "Open", "Save", "Save as...", "Close"]
Edit = ["Undo", "Redo", "Cut", "Copy", "Paste", "Find", "Replace"]
View = ["Search", "Run", "Extensions", "Appearance", "Testing"]
Help = ["Get Started", "Documentation", "Tips and Tricks", "Privacy statement", "About"]

#main menues dict which will be visible in the menubar 
menu_list = {"File": File, "Edit" : Edit , "View" : View, "Help" : Help}


#creating the main menubar
menubar = tk.Menu(root, tearoff=0)
root.config(menu=menubar)

for menu_name in menu_list:
    created_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=menu_name, menu=created_menu)

    for submenu in menu_list[menu_name]:
        created_menu.add_command(label=submenu)


root.mainloop()