#!/usr/bin/python3
""" returns True or False if the object is exactly
    an instance of the specified class.
"""


def is_kind_of_class(obj, a_class):
    """ Check to which class the instance belongs """

    return isinstance(obj, a_class)
