#!/usr/bin/python3

"""
This file contains the class definition of a State
and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
""" Import Modules """

Base = declarative_base()
""" creates a base class to declare data models. """

class state(Base):
    """ Class state that inherits from Base """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                    autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
