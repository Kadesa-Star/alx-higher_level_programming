#!/usr/bin/python3
"""
Script to delete allState objects withname containing letter 'a' from database
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

    # Query and delete State objects with name containing 'a'
    states_to_delete = (session.query(State)
                        .filter(State.name.like('%a%')).all())
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close session
    session.close()
