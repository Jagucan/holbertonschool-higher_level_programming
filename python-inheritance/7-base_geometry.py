#!/usr/bin/python3
""" returns True or False if the object is exactly
    an instance of the specified class.
"""


class BaseGeometry:
    """ Base for geometric figures. """

    def area(self):
        """ Return the area """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if value is an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
