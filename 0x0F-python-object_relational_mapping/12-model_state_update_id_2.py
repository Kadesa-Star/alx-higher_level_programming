#!/usr/bin/python3
"""
Script to change the name of a State object from the database hbtn_0e_6_usa.
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

    # create a new State object
    state_to_update = session.query(State).filter_by(id=2).first()

    # update the name of the State object
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
    else:
        print("Not found")

    # Close session
    session.close()
