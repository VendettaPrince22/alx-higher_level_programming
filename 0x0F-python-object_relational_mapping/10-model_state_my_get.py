#!/usr/bin/python3
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MY_USER = sys.argv[1]
MY_PASS = sys.argv[2]
MY_DB = sys.argv[3]
search_name = sys.argv[4]

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(MY_USER, MY_PASS, MY_DB), pool_pre_ping=True)
Session = sessionmaker(bind=engine)

session = Session()

for id, in session.query(State.id)\
        .filter(State.name == '{:s}'.format(search_name)):
    print("{}".format(id))
