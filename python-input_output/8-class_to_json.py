#!/usr/bin/python3
""" Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object
"""


def class_to_json(obj):
    """ Class to JSON """

    desc = {}
    for l, val in obj.__dict__.items():
        if isinstance(val, (list, dict, str, int, bool)):
            desc[l] = val
    return desc
