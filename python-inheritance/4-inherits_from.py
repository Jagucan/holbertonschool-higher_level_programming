#!/usr/bin/python3
""" returns True or False if the object is exactly
    an instance of the specified class.
"""


def inherits_from(obj, a_class):
    """ Check to which class the instance belongs """

    return issubclass(type(obj), a_class)
