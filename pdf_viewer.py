#import sections
import tkinter as tk
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import filedialog

#tk initialization
window = tk.Tk()
window.title("Pdf Viewer")
window.geometry("600x720")

#Menu bar
menubar = tk.Menu(window, tearoff=0)
filemenu = tk.Menu(menubar, tearoff=0)

#this function will open pdf when file is chosen from the open menu
def openPdf():
    show_pdf = pdf.ShowPdf()
    open_dialog = filedialog.askopenfile(initialdir="/home/mehrub/Downloads/")
    view_pdf = show_pdf.pdf_view(window, pdf_location=open_dialog)
    view_pdf.pack()

#Menus used in the script
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label='open', command=openPdf)







window.config(menu=menubar)
window.mainloop()
