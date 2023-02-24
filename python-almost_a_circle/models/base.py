#!/usr/bin/python3
""" Base module """
import json


class Base:
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
        """ Writes the JSON string representation of list_objs """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance with attributes from a dictionary """
        if cls.__name__ == "Rectangle":
            width = dictionary.get("width", 1)
            height = dictionary.get("height", 1)
            instance = cls(width, height)
        elif cls.__name__ == "Square":
            size = dictionary.get("size", 1)
            instance = cls(size)
        else:
            instance = cls()
        return instance

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as f:
                json_string = f.read()
                list_dict = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []
