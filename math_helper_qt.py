from PyQt5.QtWidgets import QApplication, QVBoxLayout, QGroupBox, QWidget, QPushButton, QHBoxLayout, QGridLayout, QLineEdit, QLabel

class MathApp(QWidget):
    def __init__(self):
        super(MathApp, self).__init__()
        self.initUI()
        
    def initUI(self):
        #self.setStyle('Fusion')
        self.setWindowTitle("Math Helper!")
        self.formula_list = {('Quadratic Formula',self.setup_quad),
                             ('Pythagorean Theorem',self.setup_pythag)}
        self.layout = QHBoxLayout()
        
        self.create_buttons()
        self.layout.addWidget(self.buttonGroupBox)
        # main containers
        #self.button_frame = QGridLayout()
        #self.function_frame = QGridLayout()
        #self.result_label = QLabel('')
        #self.function_frame.addWidget(self.result_label,0,4)
        #self.layout.addWidget(self.button_frame)
        #self.layout.addWidget(self.function_frame)
        self.setLayout(self.layout)
        self.show()


    def create_buttons(self):
        self.buttonGroupBox = QGroupBox()
        layout = QGridLayout()
        #layout.setColumnStretch(1,4)
        #layout.setColumnStretch(2,4)
        
        quad_button = QPushButton('Quadratic Formula')
        quad_button.clicked.connect(self.setup_quad)
        layout.addWidget(quad_button,0,0)
        
        pyth_button = QPushButton('Pythagorean Theorem')
        pyth_button.clicked.connect(self.setup_pythag)
        layout.addWidget(pyth_button,1,0)
        
        self.buttonGroupBox.setLayout(layout)
        
    
    
    def setup_quad(self):
        ''' setup entries for quadratic formula
        '''
        self.functionGroupBox = QGroupBox()
        layout = QGridLayout()
        
        
        
        # create input labels and entries
        func_label = QLabel('ax^2 + bx + c = 0')
        layout.addWidget(func_label,0,0)
        layout.setRowStretch(0,2)
        a_label = QLabel('a:')
        layout.addWidget(a_label,1,0)
        a = QLineEdit()
        layout.addWidget(a,1,1)
        b_label = QLabel('b:')
        layout.addWidget(b_label,2,0)
        b = QLineEdit()
        layout.addWidget(b,2,1)
        c_label = QLabel('c:')
        layout.addWidget(c_label,3,0)
        c = QLineEdit()
        layout.addWidget(c,3,1)
        
        
        # create and place evaluate button
        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(lambda: self.qf(a.getText(),b.getText(),c.getText()))
        layout.addWidget(calc_button,4,0)
        layout.setRowStretch(4,2)
        
        self.functionGroupBox.setLayout(layout)
        
        self.layout.addWidget(self.functionGroupBox)
                    
    
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
    
    
    def setup_pythag(self):
        ''' setup entries for pythagorean theorem
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
        calc_button = Button(self.function_frame,text="Calculate",command=lambda: self.pt(a.get(),b.get(),c.get()))
        calc_button.grid(row=3,columnspan=2,sticky='ew')
    
        
    
    def pt(self, a, b, c):
        ''' find the missing side and display the result
        '''
        
        self.result_label.destroy()
        
        # Determine which side needs to be calculated
        if a == '' and not b == '' and not c == '':
            a = 0
            b = float(b)
            c = float(c)
            
        elif b == '' and not a == '' and not c == '':
            a = float(a)
            b = 0
            c = float(c)
        
        elif c == '' and not a == '' and not b == '':
            a = float(a)
            b = float(b)
            c = 0
            
        else:
            self.result_label = Label(self.function_frame,text="Leave missing side empty.")
            self.result_label.grid(row=4,columnspan=2)
            return
        
        try:
            print(a,b,c)
            result = pythag_theorem(a,b,c)
            self.result_label = Label(self.function_frame,text=result)
            self.result_label.grid(row=4,columnspan=2)
            
        except ValueError as e:
            self.result_label = Label(self.function_frame,text=e)
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


def pythag_theorem(a,b,c):
    ''' uses the pythagorean theorem to find the length of a
        missing side in a right triangle.  The side with length
        0 is the missing side
    
        >>> pythag_theorem(3,4,0)
        'c = 5.0'
        
        >>> pythag_theorem(0,4,5)
        'a = 3.0'
        
        >>> pythag_theorem(3,0,5)
        'b = 4.0'
        
        >>> pythag_theorem(0,0,0)
        Traceback (most recent call last):
        ...
        ValueError: Only one side may be 0
        
        >>> pythag_theorem(-1,-1,-1)
        Traceback (most recent call last):
        ...
        ValueError: side lengths must be positive

    '''
    from math import sqrt
    if a < 0 or b < 0 or c < 0:
        raise ValueError("side lengths must be positive")
    
    elif a == 0 and not b == 0 and not c == 0:
        return 'a = ' + str(round(sqrt(c**2 - b**2),3))

    
    elif b == 0 and not a == 0 and not c == 0:
        return 'b = ' + str(round(sqrt(c**2 - a**2),3))
    
    
    elif c == 0 and not a == 0 and not b == 0:
        return 'c = ' + str(round(sqrt(a**2 + b**2),3))

    else:
        raise ValueError("Only one side may be 0")

def main():
    app = QApplication([])
    my_gui = MathApp()
    app.exec_()
    

if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
    #doctest.run_docstring_examples(pythag_theorem,globals())
    _