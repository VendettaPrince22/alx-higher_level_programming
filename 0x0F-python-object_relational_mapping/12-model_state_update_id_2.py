#!/usr/bin/python3
"""Changes the name of a State object"""
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

    update_state = session.query(State).filter(State.id == 2).\
        update({State.name == 'New Mexico'})

    session.commit()
