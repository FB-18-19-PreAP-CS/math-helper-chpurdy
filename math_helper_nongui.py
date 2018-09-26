
def run_qf():
    ''' get user input, evaluate the quadratic formula, and display results
    '''
    print()
    print('To use the quadratic formula, I need values for')
    print('the coefficients in the equation ax^2 + bx + c = 0')
    print()
    # Check for any missing inputs/convert inputs to integers
    while True:
        try:
            a = float(input('a: '))
            b = float(input('b: '))
            c = float(input('c: '))
            break
        except ValueError:
            print('a, b, and c must be real numbers')
    
    result = quadratic_formula(a,b,c)
    if result is None:
        disp = 'No Solution'
        
    elif isinstance(result,float):
        disp = f'{result:.2f}'
        
    else:
        disp = f'{result[0]:.2f}' + ' and ' + f'{result[1]:.2f}'
    
    print(f'Solution:\n{disp}')


def run_pythag():
    ''' find the missing side and display the result
    '''
    print()
    print('To use the Pythagorean Theorem, I need values for')
    print('two of the sides in a triangle.')
    print()
    print('Enter 0 for the length of the side you wish to')
    print('find.  Remember, C must be the LONGEST side')
    print()
    
 
    # Determine which side needs to be calculated
    while True:
        a = input('a: ')
        b = input('b: ')
        c = input('c: ')
        if a == '0' and not b == '0' and not c == '0':
            a = 0
            b = float(b)
            c = float(c)
            break
            
        elif b == '0' and not a == '0' and not c == '0':
            a = float(a)
            b = 0
            c = float(c)
            break
        
        elif c == '0' and not a == '0' and not b == '0':
            a = float(a)
            b = float(b)
            c = 0
            break
            
        else:
            print('You must put 0 in for ONE of the sides!')
    
    try:
        print(pythag_theorem(a,b,c))
        
    except ValueError as e:
        showinfo("Error:",e)
    



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
    print("Welcome to Mr. Purdy's Math Helper!")
    quit = False
    while not quit:
        print("Available Formulas:")
        print("(1) Quadratic Formula")
        print("(2) Pythagorean Theorem")
        print("(3) Quit")
        print("Type the number of your choice and press enter.")
        try:
            choice = int(input("> "))
            if choice < 1 and choice > 3:
                print("Invalid option!")
                print()
                continue
            
        except:
            print("Invalid Input")
            
        if choice == 1:
            run_qf()
        elif choice == 2:
            run_pythag()
        elif choice == 3:
            print("I hope I helped.")
            return
        else:
            print("Something went wrong!")
        
        while True:
            print("Would you like to solve another problem? y/n")
            try:
                choice = input("> ").lower()
                if choice == 'n':
                    quit = True
                    print("I hope I helped!")
                    break
                elif choice == 'y':
                    break
                else:
                    print("Invalid input")
            except:
                print('Invalid input')
                
            
    

if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
    #doctest.run_docstring_examples(pythag_theorem,globals())
    