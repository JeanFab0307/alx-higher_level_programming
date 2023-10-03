#!/usr/bin/python3
"""
This script lists all State objects that contains 'a'
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    value = argv[4].partition(";")
    if value[1] == ";":
        value = value[0][:-1]
    else:
        value = value[0]

    for instance in session.query(State).filter(State.name == value):
        print(instance.id)
        quit()
    print("Not found")
