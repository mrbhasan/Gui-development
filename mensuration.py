import tkinter as tk 
import tkinter.ttk as ttk 
import tkinter.messagebox as messagebox 
import math


class Area_of_triangular_region:
    @staticmethod

    def right_angled_triangle(a, b):
        #1/2*a*b
        result = 1/2*a*b
        if format:
            return f'the result is {result}'

        return result

       
    @staticmethod
    def two_side_and_region(a, b, deg):
        #1/2*sinC
        if deg == 30:
            sin_val = 1/2
        elif deg== 45:
            sin_val = 1/math.sqrt(2)
        elif deg == 60:
            sin_val = math.sqrt(3)/2
        elif deg == 90:
            sin_val = 1

        result = 1/2*a*b*sin_val
        if format:
            return f'the result is {result}'

        return result


class InputFrame(tk.Frame):
    def __init__(self, container, frameno):
        self.frameno = frameno
        super().__init__(container)
        self.config(height=350, width=720)
        self.place(x=0, y=0)
        self.Create_widgets()
        

    def Create_widgets(self):
        frameno = self.frameno

        if frameno == 0:

            
            
            #first entry
            label_1 = tk.Label(self, text='Enter the value of a',  pady=5)
            label_1.pack()

            entry_1 = tk.Entry(self)
            entry_1.pack( pady=5)
            
           


            #2nd entry
            label_2 = tk.Label(self, text='Enter the value of b',  pady=9)
            label_2.pack()

            entry_2 = tk.Entry(self)
            entry_2.pack( pady=5)
            


            #calculate Button
            def execute():
                get_a= int(entry_1.get()) 
                get_b= int(entry_2.get())
                result = Area_of_triangular_region.right_angled_triangle(get_a, get_b)
                result_label = tk.Label(self, text= result)
                result_label.pack(side='bottom')
            
                

            calculate= tk.Button(self, text='Calculate')
            calculate.config(command=execute)
            calculate.pack()

        else:
            #first entry
            label_1 = tk.Label(self, text='Enter the value of a')
            label_1.pack()

            entry_1 = tk.Entry(self)
            entry_1.pack()

            
            #second entry
            label_2 = tk.Label(self, text='Enter the value of b')
            label_2.pack()

            entry_2 = tk.Entry(self)
            entry_2.pack()

            
            #third entry
            label_3 = tk.Label(self, text='Enter the value of degree')
            label_3.pack()

            entry_3 = tk.Entry(self)
            entry_3.pack()


            #calculate
            def execute():
                get_a= int(entry_1.get()) 
                get_b= int(entry_2.get())
                get_c = int(entry_3.get())
                result = Area_of_triangular_region.two_side_and_region(get_a, get_b, get_c)
                result_label = tk.Label(self, text= result)
                result_label.pack(side='bottom')
            
            calculate= tk.Button(self, text='Calculate')
            calculate.config(command=execute)
            calculate.pack()




class SelectionFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.config(height=150, width=720)
        self.place(x=0, y=351)
        self.create_widgets()

    def create_widgets(self):
        def get_val_1():
            get_btn_1 = btn1.get()
            InputFrame(app, get_btn_1)
            three_var_btn.deselect()
            

        def get_val_2():
            get_btn_2 = btn2.get()
            InputFrame(app, get_btn_2)
            two_varbtn.deselect()


           
                   

        btn1 = tk.IntVar()
        two_varbtn = tk.Radiobutton(self, text='Right Angled Triangle' , value=0,
         variable=btn1, command=get_val_1)
        two_varbtn.grid()

        btn2 = tk.IntVar()
        three_var_btn = tk.Radiobutton(self, text='Two Side and A Region', value=1,
        variable=btn2, command=get_val_2)
        
        three_var_btn.grid()

       

        


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mensuration")
        self.geometry("720x500")
        self.resizable(False, False)

        SelectionFrame(self)



app = App()
app.mainloop()





