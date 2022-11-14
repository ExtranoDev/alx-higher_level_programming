#!/usr/bin/python3
"""Python file that works with SQLAlchemy"""

from sqlalchemy import Column, String, Integer
from model_state import Base


class State(Base):

    """Model state class"""

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False,
                      ForeignKey('states.id'))
