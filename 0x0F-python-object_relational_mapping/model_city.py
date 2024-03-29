#!/usr/bin/python3
"""Python file that works with SQLAlchemy"""

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):

    """Model state class"""

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
