#!/usr/bin/python3
""" Module that returns the list
    of available attributes
"""


def lookup(obj):
    """ Returns the list of available attributes and methods of an object. """
    return [atributo for atributo in dir(obj)\
        if not callable(getattr(obj, atributo)) and not atributo.startswith("__")]
