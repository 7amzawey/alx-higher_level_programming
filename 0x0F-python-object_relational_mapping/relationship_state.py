#!/usr/bin/python3
"""
this module is a MySQLalchemy Module to define the declarative base class
which State is a class in it
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    States Class:
    - Ingerits from Base
    - Links to the MySQL table 'states'
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all")
