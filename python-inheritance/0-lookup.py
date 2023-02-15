#!/usr/bin/python3
""" Module that returns the list
    of available attributes
"""


def lookup(objeto):
    """ Returns the list of available attributes
        and methods of an object
    """
    attributes = dir(object)
    attribute_list = []
    for attributes in attributes:
        if not callable(getattr(object, attributes)) and not attributes.startswith("__"):
            attribute_list.append(attributes)
    return attribute_list
