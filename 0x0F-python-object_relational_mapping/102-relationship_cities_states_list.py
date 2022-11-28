#!/usr/bin/python3
"""script that lists all City objects from the database"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def list_cities():
    """function lists cities"""

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(City, State).filter(City.state_id == State.id)\
            .order_by(City.id).all()
    for city, state in rows:
        print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()

if __name__ == '__main__':
    list_cities()
