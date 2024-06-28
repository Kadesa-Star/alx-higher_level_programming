# 14-model_city_fetch_by_state.py

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    # Create a configured "Session" class
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all City objects, sorted by id
    cities = session.query(City).order_by(City.id).all()

    # Print results in the required format
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close session
    session.close()
