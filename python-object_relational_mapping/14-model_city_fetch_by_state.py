#!/usr/bin/python3
"""
Prints the all the cities from the data base
"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(
        State, City).join(
            State, City.state_id == State.id).order_by(City.id).all()

    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
