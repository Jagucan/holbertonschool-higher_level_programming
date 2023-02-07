#!/usr/bin/python3
""" Module that defines the Square class.

    This module provides a class called Square,
    that can be used to create square objects.
"""


class Square:
    """ This is the Square class. """

    def __init__(self, size=0):
        """ Initializes a new instance of the Square class """
        self.__size = size

    """ @property
        - Decorator that allows converting a method to attribute.
        - Used to retrieve the value of the property
        - getter metode.
    """
    @property
    def size(self):
        """ Instance of the Square class,
            to get the value of the private attribute "_size".
        """
        return self.__size

    """ @size.setter
        - Decorator that allows converting a method to attribute.
        - Is used to set a new value for the property.
        - getter metode.
    """
    @size.setter
    def size(self, value):
        """ Instance of the Square class,
            to set a new value for the private attribute "_size"
        """
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        

    def area(self):
        """ Instance of the Square class,
            to return the current square area
        """
        return self.__size ** 2

