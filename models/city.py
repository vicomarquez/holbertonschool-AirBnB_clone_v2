#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import environ


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    # initialize class for file/db storage type
    if environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = 'cities'

        name = Column(String(128), nullable=False)

        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ''
        state_id = ''
