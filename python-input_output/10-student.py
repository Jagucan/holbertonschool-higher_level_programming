#!/usr/bin/python3
""" Student to JSON with filter """


class Student:
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ Initialize instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__
        else:
            attrs_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attrs_dict[attr] = getattr(self, attr)
            return attrs_dict
