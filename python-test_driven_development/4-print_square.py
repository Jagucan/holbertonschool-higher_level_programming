#!/usr/bin/python3
""" The function that prints a square with the character #.
"""


def print_square(size):
    """ Checks if size is an int or float greater than 0.
        if it is it prints a square
    """

    if type(size) is not int:
    
        if type(size) is float and size < 0:
            raise TypeError("size must be an integer")
    
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
