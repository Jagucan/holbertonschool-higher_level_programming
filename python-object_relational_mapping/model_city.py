#!/usr/bin/python3
"""
This file  contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String
from model_state import State, Base
""" Import Modules """


class City(Base):
    """ Class state that inherits from Base """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)
