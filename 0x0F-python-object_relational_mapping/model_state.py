#!/usr/bin/python3
"""
Contains class definition of State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the Base class
Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    import sys
    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine that connects to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}\
                :{mysql_password}@localhost/{database_name}',
        pool_pre_ping=True
    )

    # Create all tables defined by Base's subclasses (State in this case)
    Base.metadata.create_all(engine)
