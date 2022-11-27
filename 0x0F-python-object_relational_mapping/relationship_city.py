#!/usr/bin/python3
"""Python file that works with SQLAlchemy"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base
from relationship_state import Base, State


class City(Base):

    """Model state class"""

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
>>>>>>> parent of 4f4af21... merge
