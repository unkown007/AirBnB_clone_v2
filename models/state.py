#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE', '') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
                'City',
                back_populates='state',
                cascade='all, delete, delete-orphan')

        def __init__(self, *args, **kwargs):
            """ initialize new object """
            super().__init__(*args, **kwargs)
else:
    class State(BaseModel):
        """ State class """
        name = ''

        def __init__(self, *args, **kwargs):
            """ Initialize a new object """
            super().__init__(*args, **kwargs)

        @property
        def cities(self):
            """ return a list of City instances with state_id
            equals to the current State.id """
            all_cities = models.storage.all('City')
            tmp = []
            for cid in all_cities:
                if all_cities[cid].state_id == self.id:
                    tmp.append(all_cities[cid])
            return tmp
