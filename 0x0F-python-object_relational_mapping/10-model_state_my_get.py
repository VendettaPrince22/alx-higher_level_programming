#!/usr/bin/python3
"""Prints the State object with name passed as argument"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    search_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(MY_USER, MY_PASS, MY_DB),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    instance = session.query(State).filter(State.name == (search_name,))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
