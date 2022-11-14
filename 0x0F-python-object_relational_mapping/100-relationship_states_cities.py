#!/usr/bin/python3
"""Script creates State “California” with City “San Francisco”
from the database"""


from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    """creates the State “California” with the
    City “San Francisco” from the database"""

    # create engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))

    # create tables
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # new object
    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)

    # save created object
    session.add(state)
    session.commit()
    session.close()
