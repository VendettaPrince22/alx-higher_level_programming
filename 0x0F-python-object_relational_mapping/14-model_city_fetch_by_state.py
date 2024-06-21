#!/usr/bin/python3
"""Prints all City objects from database"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_objects = session.query(State.name, City.id, City.name)\
        .join(City).all()

    for x in cities_objects:
        print("{}: ({}) {}".format(x[0], x[1], x[2]))
