#!/usr/bin/python3
"""
State module
"""

from models.base_model import BaseModel
from models.city import City
from models import storage
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel):
    """
    State class
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """
            Getter attribute that returns the list of City instances with state_id
            equals to the current State.id
            """
            city_list = []
            for city_id, city in storage.all(City).items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
