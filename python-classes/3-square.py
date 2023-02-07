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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Initializes an instance of the Square class,
            to return the current square area
        """
        return self.__size ** 2
