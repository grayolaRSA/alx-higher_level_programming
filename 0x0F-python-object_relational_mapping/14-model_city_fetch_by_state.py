#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all City objects sorted by id
    cities = session.query(City).order_by(City.id).all()

    # Print the City objects
    for city in cities:
        state_name = session.query(State.name).\
            filter(State.id == city.state_id).order_by(City.id.asc()).scalar()
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    # Close the session
    session.close()
