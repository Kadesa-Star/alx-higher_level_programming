#!/usr/bin/python3
"""
Script to print the first state object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # Create a session
    session = Session()

    # Query all State objects, sorted by id
    states = (session.query(State)
              .filter(State.name.like('%a%'))
              .order_by(State.id).all())

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
