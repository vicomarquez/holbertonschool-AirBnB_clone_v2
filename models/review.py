#!/usr/bin/python3
"""This is the review class"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    if models.storage_type = 'db':
        __tablename__ = "reviews"

        place_id = Column(String(60), ForeignKey('places.id') nullable=False)
        user_id = Column(String(60), ForeignKey('users.id')nullable=False)
        text = Column(String(1024), nullable=False)
    
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """ initialize Review """
        super().__init__(*args, **kwargs)
