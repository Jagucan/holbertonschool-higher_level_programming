#!/usr/bin/python3
""" returns True or False if the object is exactly
    an instance of the specified class.
"""


class BaseGeometry:
    """_summary_
    """

    def area(self):
        """_summary_
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """_summary_
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """_summary_
    """

    def __init__(self, width, height):
        """ Initialize a new Rectangle instance """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
