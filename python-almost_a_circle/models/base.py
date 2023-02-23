#!/usr/bin/python3
""" Base module """
import json



class Base():
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize instance """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string representation """
        if list_dictionaries is None or len(list_dictionaries) == 0:        
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save Object to file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            list = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list))
