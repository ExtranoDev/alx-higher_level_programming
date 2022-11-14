#!/usr/bin/python3
"""Python file that works with SQLAlchemy"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):

    """Model state class"""

    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False,
                autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          cascade='all, delete-orphan', backref='state')
