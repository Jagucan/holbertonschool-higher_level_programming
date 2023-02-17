#!/usr/bin/python3
""" Returns the geometric figure """


class BaseGeometry:
    """ Base for geometric figures. """

    def integer_validator(self, name, value):
        """ Validate fon an integer. """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle Class """

    def __init__(self, width, height):
        """ Initialize a new Rectangle instance """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the rectangle Area."""

        width = self.__width
        height = self.__height
        result = width * height
        return result


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size):
        """ Initialize a new Square instance """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Return the Square description. """

        return ("[Square] {}/{}" .format(self.__size, self.__size))
