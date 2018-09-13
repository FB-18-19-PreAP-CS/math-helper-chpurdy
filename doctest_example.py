'''  Here is an example of how doctesting works
     you should work on creating your tests
     as part of writing your functions
     
     This program initially fails 3 of the tests
     intentionally so you can see what failures look like
'''

import math

PHI = (1 + math.sqrt(5)) / 2  # Golden Ratio

def fib(n):
    ''' returns the nth number in the
        Fibonacci sequence
    
    >>> fib(2)
    1
    
    >>> fib(5)
    5
    
    >>> fib(10)
    55
    
    There are no negative Fibonacci numbers
    >>> fib(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be positive
    
    There are no fractional Fibonacci numbers
    >>> fib(3.5)
    Traceback (most recent call last):
        ...
    ValueError: n must be an exact integer
    
    It can't be too large either
    >>> fib(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n is too large
    '''
    if n <= 0:
        raise ValueError("n must be positive")
    
    if math.floor(n) != n:
        raise ValueError("n must be an exact integer")
    
    if n+1 == n: #catches a value like 1e100
        raise OverflowError("n is too large")
    
    # Here is the magic formula:
    return int((PHI**n - (-1/PHI)**n)/math.sqrt(5))
    
    
    # change the return statement to the line below
    # in order to resolve the errors
    # return int((PHI**n - (-1/PHI)**n)/math.sqrt(5))
                
if __name__ == "__main__":
    import doctest
    doctest.testmod()