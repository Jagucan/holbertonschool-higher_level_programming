#!/usr/bin/python3
""" Simple Rectangle """


class Rectangle:
    """ This is the Rectangle class. """

    def __init__(self, widht=0, height=0):
        """ Initializes a new instance of the Rectangle class """

        self.__widht = widht
        self.__height = height

    @property
    def widht(self):
        """ Instance of the Rectangle class,
            to get the value of the private attribute "__widht".
        """
        return self.__widht

    @widht.setter
    def widht(self, value):
        """ Instance of the Rectangle class,
            to set a new value for the private attribute "__widht"
        """
        self.__widht = value

        if not isinstance(value, int):
            raise TypeError("widht must be an integer")
        if value < 0:
            raise ValueError("widht must be >= 0")

    @property
    def height(self):
        """ Instance of the Rectangle class,
            to get the value of the private attribute "__height".
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Instance of the Rectangle class,
            to get the value of the private attribute "__height".
        """
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
