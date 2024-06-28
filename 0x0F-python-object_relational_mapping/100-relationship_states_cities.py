#!/usr/bin/python3
"""Creates new state with city"""
import sys
from relationship_city import City, Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California', cities=City(name='San Francisco'))
    session.add(new_state)

    session.commit()
