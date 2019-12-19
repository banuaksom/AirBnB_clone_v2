#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from slqalchemy import Column, String
from slqalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
