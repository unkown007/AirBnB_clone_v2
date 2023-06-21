#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4


if getenv('HBNB_TYPE_STORAGE', '') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(
                String(60),
                ForeignKey('states.id'),
                nullable=False)
        state = relationship('State', back_populates='cities')

        def __init__(self, *args, **kwargs):
            """ initialize new object """
            setattr(self, 'id', str(uuid4()))
            for key, value in kwargs.items():
                setattr(self, key, value)
else:
    class City(BaseModel):
        """ The city class, contains state ID and name """
        state_id = ""
        name = ""
