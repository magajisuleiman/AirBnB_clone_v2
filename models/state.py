#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    
    envv = getenv('HBNB_TYPE_STORAGE')
    if envv =='db':
        name = Column(String(128), nullable=False)
    else:
        ''' the file storage relation '''
        @property
        def cities(self):
            ''' for returning the list of City instances'''
            from models import storage
            from models.city import City

            c_list = []
            c_dict = storage.all(City)

            for c in c_dict.values():
                if c.state_id == self.id:
                    c_list.append(c)
            return c_list
