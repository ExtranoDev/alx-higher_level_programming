#!/usr/bin/python3
"""script lists all State objects,
and corresponding City objects, contained in the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City


def list_state_city():
    """Lists States and cities in them"""

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).all()
    for state in rows:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()

if __name__ == '__main__':
    list_state_city()
