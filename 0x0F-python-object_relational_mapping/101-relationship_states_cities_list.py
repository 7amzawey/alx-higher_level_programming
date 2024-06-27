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
    states = session.query(
            State).options(
                    joinedload(State.cities)).all()

    states_sorted = sorted(
            states, key=lambda s: (s.id, [c.id for c in s.cities]))
    for state in states_sorted:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
