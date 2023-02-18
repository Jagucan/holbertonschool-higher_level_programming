#!/usr/bin/python3
""" Creates an Object from a “JSON file” """


import json
"import JSON"


def load_from_json_file(filename):
    """ Create object from a JSON file """

    with open(filename, "r") as file:
        obj = json.load(file)
        return obj
