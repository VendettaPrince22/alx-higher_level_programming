#!/usr/bin/python3
"""Deletes all State objects with name containing letter a"""
import sys
from model_state import Base, State
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

    del_item = session.query(State).filter(State.name.like('%a%'))\
        .delete(synchronize_session='fetch')

    session.commit()
