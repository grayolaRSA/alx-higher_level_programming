#!/usr/bin/python3
"""
Update state with id=2 to New Mexico
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    updateState = session.query(State).filter(State.id == 2).first()

    if updateState:
        updateState.name = 'New Mexico'
        session.commit()

    print(newState.id)
