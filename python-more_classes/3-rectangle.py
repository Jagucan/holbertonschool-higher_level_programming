#!/usr/bin/python3
""" Simple Rectangle """


class Rectangle:
    """ This is the Rectangle class. """

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of the Rectangle class """

        self.__width = width
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """ Instance of the Rectangle class,
            to get the value of the private attribute "__width".
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Instance of the Rectangle class,
            to set a new value for the private attribute "__width"
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Instance of the Rectangle class,
            to return the current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Instance of the Rectangle class,
            to return the current perimeter area
        """
        if self.__height != 0 or self.__height != 0:
            return (self.__width + self.__height) * 2
        else:
            return 0

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)
