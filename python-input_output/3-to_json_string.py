#!/usr/bin/python3
""" Returns the JSON representation of an object (string) """


import json
""" Import JSON Module"""


def to_json_string(my_obj):
    """ JSON - string """

    return json.dumps(my_obj)
