from tkinter import *




class MathApp:
    def __init__(self, master):
        self.master = master
        master.title("Math Helper!")
        self.formula_list = {('Quadratic Formula',self.quad),('Test Formula',self.test)}
        
        # main containers
        self.button_frame = Frame(height=2, bd=1, relief="sunken")
        self.function_frame = Frame(height=500,width=500,bd=1)

        #layout main containers
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.function_frame.grid_columnconfigure(0, weight=1)
        #place main containers
        self.button_frame.grid(row=0, column=0, sticky="ns")
        self.function_frame.grid(row=0, column=1, sticky="nsew")
        
        for counter, formula in enumerate(self.formula_list):
            Button(self.button_frame,text=formula[0],command=formula[1]).grid(row=counter+2,column=0,sticky="w")
        
        self.button_label = Label(self.button_frame, text="This is some text")
        self.button_label.grid(row=1, column=0, sticky="w")
        

        
    def greet(self):
        print("Cool")
        
    def quad(self):
        ''' setup entries for quadratic formula
        '''
        # get rid of everything in the function frame
        for widget in self.function_frame.winfo_children():
            widget.destroy()
        
        # create input labels and entries
        a_label = Label(self.function_frame,text='a:')
        a = Entry(self.function_frame)
        b_label = Label(self.function_frame,text='b:')
        b = Entry(self.function_frame)
        c_label = Label(self.function_frame,text='c:')
        c = Entry(self.function_frame)
        
        # place input labels and entries
        a_label.grid(row=0,column=0,sticky='ew')
        a.grid(row=0,column=1,sticky='ew')
        b_label.grid(row=1,column=0,sticky='ew')
        b.grid(row=1,column=1,sticky='ew')
        c_label.grid(row=2,column=0,sticky='ew')
        c.grid(row=2,column=1,sticky='ew')
        
        # create and place evaluate button
        calc_button = Button(self.function_frame,text="Calculate",command=lambda: qf(int(a.get()),int(b.get()),int(c.get())))
        calc_button.grid(row=3,columnspan=2,sticky='ew')
        
    def test(self):
        # get rid of everything in the function frame
        for widget in self.function_frame.winfo_children():
            widget.destroy()
            
        print('test')




def qf(a,b,c):
    from math import sqrt
    print(a,b,c)
    print((-b + sqrt(b**2 - 4*a*c))/(2*a))


def my_func(a,b):
    ''' returns a particular formula that I made up
    '''
    return a + b - a * b -c

def main():
    root = Tk()
    my_gui = MathApp(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()
    
    