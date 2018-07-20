#!/usr/bin/python3
"""Adds a new State object (Louisiana) to the database hbtn_0e_6_usa
   takes arguments: mysql-username, mysql-password, database-name
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    louis = State(name='Louisiana')
    session.add(louis)
    session.commit()

    state = session.query(State).filter(State.name == 'Louisiana').first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
