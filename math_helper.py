from tkinter import *

class MathApp:
    def __init__(self, master):
        self.master = master
        master.title("Math Helper!")
        self.formula_list = {('Quadratic Formula',self.setup_quad),('Test Formula',self.test)}
        
        
        # main containers
        self.button_frame = Frame(height=2, bd=1, relief="sunken")
        self.function_frame = Frame(height=0,width=0,bd=1)
        self.result_label = Label(self.function_frame,text='')
        
        #layout main containers
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.function_frame.grid_columnconfigure(0, weight=1)
        #place main containers
        self.button_frame.grid(row=0, column=0, sticky="ns")
        self.function_frame.grid(row=0, column=1, sticky="nsew")
        
        for counter, formula in enumerate(self.formula_list):
            Button(self.button_frame,text=formula[0],command=formula[1]).grid(row=counter+2,column=0,sticky="w")
        
        self.button_label = Label(self.button_frame, text="Available Formulas")
        self.button_label.grid(row=1, column=0, sticky="w")
        
        
    def setup_quad(self):
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
        calc_button = Button(self.function_frame,text="Calculate",command=lambda: self.qf(a.get(),b.get(),c.get()))
        calc_button.grid(row=3,columnspan=2,sticky='ew')
        
        
    def test(self):
        # get rid of everything in the function frame
        for widget in self.function_frame.winfo_children():
            widget.destroy()
            
        print('test')

    def qf(self, a, b, c):
        ''' evaluate the quadratic formula and display results
        '''
        self.result_label.destroy()
        
        # Check for any missing inputs/convert inputs to integers
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except ValueError:
            self.result_label = Label(self.function_frame,text="Missing Input")
            self.result_label.grid(row=4,columnspan=2)
            return
        
        result = quadratic_formula(a,b,c)
        if result is None:
            disp = 'No Solution'
            
        elif isinstance(result,float):
            disp = f'{result:.2f}'
            
        else:
            disp = f'{result[0]:.2f}' + ' and ' + f'{result[1]:.2f}'
        
        self.result_label = Label(self.function_frame,text=disp)
        self.result_label.grid(row=4,columnspan=2)
        
    
def quadratic_formula(a,b,c):
    ''' returns the results from the quadratic formula
        
        Two solutions returns a tuple of floats
        >>> quadratic_formula(1,3,2)
        (-1.0, -2.0)
        
        >>> quadratic_formula(1,5,2)
        (-0.438447, -4.561553)
        
        >>> quadratic_formula(-3,7,1)
        (-0.135042, 2.468375)
        
        No solution returns None
        >>> quadratic_formula(1,1,1)
        
        
        >>> quadratic_formula(1,0,-4)
        (2.0, -2.0)
        
        One solution returns a float
        >>> quadratic_formula(1,-4,4)
        2.0
        
    '''
    from math import sqrt
    if b**2 - 4*a*c < 0:
        return None
    
    elif b**2 - 4*a*c == 0:
        return round(-b/(2*a),6)
    
    else:
        return (round((-b + sqrt(b**2 - 4*a*c))/(2*a),6), round((-b - sqrt(b**2 - 4*a*c))/(2*a),6))


def main():
    root = Tk()
    my_gui = MathApp(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
    
    