#!/usr/bin/python3
"""Script list objects in a database"""


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

    rows = session.query(State).filter(State.name.ilike(
        '%a%')).order_by(State.id)
    for row in rows:
        print("{}: {}".format(row.id, row.name))
    session.close()
