#!/usr/bin/python3
"""
this module is a MySQLalchemy Module to define the declarative base class
which cities is a class in it
"""


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    States City:
    - Ingerits from Base
    - Links to the MySQL table 'cities'
    """
    __tablename__ = 'cities'
    id = Column(
            Integer, primary_key=True,
            unique=True,
            autoincrement=True,
            nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates="cities")


if __name__ == "__main__":

    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
