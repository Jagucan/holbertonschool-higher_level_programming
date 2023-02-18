#!/usr/bin/python3
""" Returns the JSON representation of an object (string) """


import json
""" Import JSON Module"""


def from_json_string(my_str):
    """ JSON - string to objet """

    return json.loads(my_str)
