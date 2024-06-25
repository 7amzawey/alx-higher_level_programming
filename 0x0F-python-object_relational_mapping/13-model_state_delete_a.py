#!/usr/bin/python3
"""
this module is for a function that delets everystate with an a
"""

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
    this function is going to delete every state with an A
    """
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

    states = session.query(
            State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        session.delete(state)
    session.commit()

session.close()
