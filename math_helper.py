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
        
        self.greet_button = Button(self.button_frame, text="Greet",command=self.greet)
        self.greet_button.grid(row=1, column=1)
        
        self.close_button = Button(self.button_frame, text="Close",command=master.quit)
        self.close_button.grid(row=1,column=2)
        
        self.function_label = Label(self.function_frame,text="test")

        
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
        
        # place input labels and entries
        a_label.grid(row=0,column=0,sticky='nsew')
        a.grid(row=0,column=1,sticky='nsw')
        
    def test(self):
        print('test')







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
    
    