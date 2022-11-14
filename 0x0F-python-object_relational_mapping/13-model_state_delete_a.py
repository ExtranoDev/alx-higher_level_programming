#!/usr/bin/python3
"""script that deletes a State object with name containing 'a'
from a database

Script should:
    take 3 arguments: mysql username, mysql password and database name
    You must use the module SQLAlchemy
    You must import State and Base from model_state
    from model_state import Base, State
    Your script should connect to a MySQL server
    running on localhost at port 3306
    Results must be sorted in ascending order by states.id
    The results must be displayed as they are in the example below
    Your code should not be executed when imported"""


if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
