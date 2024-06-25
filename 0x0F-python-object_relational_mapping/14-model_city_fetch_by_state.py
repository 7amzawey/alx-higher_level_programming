#!/usr/bin/python3
"""
This is gonna list all the objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

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
    cities = session.query(City).all()

    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).first()
        if state:
            print(f"{state.name}: ({state.id}) {city.name}")

    session.close()
