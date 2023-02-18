#!/usr/bin/python3
""" Writes an Object to a text file, using a JSON representation """


import json
""" Import JSON Module"""


def save_to_json_file(my_obj, filename):
    """ Save Object to file """

    with open(filename, "w") as file:
        json.dump(my_obj, file)
