#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize instance """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update attributes of the rectangle """
        if len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Return string representation of Rectangle """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)
