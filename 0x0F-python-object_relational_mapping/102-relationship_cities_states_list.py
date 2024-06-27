#!/usr/bin/python3
"""
this is gonna create the state California with the city San Francisco
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import Base
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
    cities = session.query(
            City).options(
                    joinedload(City.state)).order_by(City.id).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()
