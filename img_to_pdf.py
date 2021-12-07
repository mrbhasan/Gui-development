#required module for the project
import tkinter as tk
import tkinter.messagebox as msg
import tkinter.filedialog as fd
from PIL import Image


window = tk.Tk()
window.geometry("600x500+200+100")
window.resizable(False, False)
window.title("Image to PDF Converter")


#Graphical Interface

label = tk.Label(window, text='Convert Your Images to Pdf File',
                 font=('Calibri', '20'))
label.place(x=150, y=50)


btn_font = ('Arial', '14')

select_btn = tk.Button(master=window, text='Select File',
                       bg='#63ce97', font=btn_font, padx=5, pady=5)
select_btn.place(x=250, y=110)

Convert_btn = tk.Button(master=window, text='Convert',
                        bg='#6385ce', font=btn_font, padx=5, pady=5)
Convert_btn.place(x=260, y=160)

exit_btn = tk.Button(master=window, text='Exit',
                     bg='#c1444a', font=btn_font, padx=5, pady=5)
exit_btn.place(x=270, y=210)


#functions to handle the buttons and the app
def select_file():
    global img_v2
    file_path = fd.askopenfilename(initialdir="/home/mehrub/Pictures", title="Select a Image")

    img_v1 = Image.open(file_path)
    img_v2 = img_v1.convert('RGB')


def convert_file():
    global img_v2

    file_path_out = fd.asksaveasfilename(initialfile='untitled.pdf', filetypes=[('Document Type', '.pdf')], title="Save file as")
    img_v2.save(file_path_out)
    msg.showinfo(title='Success', message="Image converted to Pdf Successfully :)")


def exit_app():
    exit_msg = msg.askyesno(
        title='Exit App', message="Are you Really wish to exit?")
    if exit_msg == True:
        window.destroy()


#connecting functions with buttons
select_btn.config(command=select_file)
Convert_btn.config(command=convert_file)
exit_btn.config(command=exit_app)


window.mainloop()
