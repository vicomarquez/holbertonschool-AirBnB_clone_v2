#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    # initialize class for file/db storage type
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)

        cities = relationship('City', cascade='all, delete', backref='state')

    else:
        name = ''

        @property
        def cities(self):
            """Getter method for cities
            Return: list of cities with state_id equal to self.id
            """
            # return list of City objs in __objects
            from models.city import City
            from models.engine import storage
            cities_dict = storage.all(City)
            cities_list = []

            # copy values from dict to list
            for value in cities_dict.keys():
                cities_list.append(value)

            return cities_list
