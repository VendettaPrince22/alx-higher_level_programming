#!/usr/bin/python3
"""Adds the State object `Louisiana` to a database"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format
                           (MY_USER, MY_PASS, MY_DB), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)

    session.commit()

    print(new_state.id)
