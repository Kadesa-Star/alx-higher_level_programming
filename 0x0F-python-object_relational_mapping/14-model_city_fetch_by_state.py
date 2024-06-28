#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State
import sys


def fetch_cities(username, password, database):
    """ Fetches and prints all cities with their corresponding state names """
    # Create an engine that connects to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)
    # Create all tables defined by Base's subclasses (City and State)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects joined with State and ordered by City.id
    cities = (session.query(City, State)
              .filter(State.id == City.state_id)
              .order_by(City.id).all())

    # Print results in the required format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Ensure correct usage with command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

# Extract command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call fetch_cities function with provided arguments
    fetch_cities(username, password, database)
