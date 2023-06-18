#!/usr/bin/python3
"""
Prints all city objects in database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    st_cit = session.query(City).order_by(City.id).all()

    for city in st_cit:
        state_name = session.query(State.name).filter(State.id == city.state_id).scalar()
        print("{}: ({}) {}".format(state_name, city.id, city.name))
