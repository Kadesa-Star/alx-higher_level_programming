#!/usr/bin/python3
# 14-model_city_fetch_by_state.py

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities(user, password, db):
    """Fetch print all City objects with their State names"""

    # Database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user, password, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects, sorted by id, with State names
    cities = session.query(City, State).filter(
        State.id == City.state_id).order_by(City.id).all()

    # Print results in the required format
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()


if __name__ == "__main__":
    # Ensure script is not executed when imported
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

fetch_cities(sys.argv[1], sys.argv[2], sys.argv[3])
