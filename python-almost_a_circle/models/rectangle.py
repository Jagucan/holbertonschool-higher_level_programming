#!/usr/bin/python3
"""
    Returns:
        _type_: _description_
"""
from models.base import Base
"""_summary_

    Returns:
        _type_: _description_
"""


class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width

    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.__width = value

    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.__height = value

    @property
    def x(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__x

    @x.setter
    def x(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.__x = value

    @property
    def y(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__y

    @y.setter
    def y(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.__y = value
