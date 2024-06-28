#!/usr/bin/python3
"""
this is gonna create the state California with the city San Francisco
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
            pool_pre_ping=True
            )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_city = City(name="mo", state_id=100)

    states = session.query(State).all()
    
    [print(state.cities[0].__dict__) for state in states]
    session.close()
