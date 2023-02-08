#!/usr/bin/python3
""" Function that adds 2 integers,
    returns the result of the sum.
"""

def add_integer(a, b=98):
    """ adds two numbers and converts them to integers
        before returning the result 
    """

    if not isinstance(a, (int, float)):
        raise TypeError ("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, (int, float)):
        a = int(a)
    if  isinstance(b, (int, float)):
        b = int(b)

    return a + b
