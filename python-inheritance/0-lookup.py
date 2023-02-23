#!/usr/bin/python3
""" Module that returns the list of available attributes
"""


def lookup(obj):
    """ returns a list of available attributes and methods of an object """
    attributes = dir(obj)
    attributes = [a for a in attributes if a.startswith('_')]
    return attributes
