#!/usr/bin/python3
"""
Defines State class and instance Base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    Class defining attributes of each state
    """

    if __name__ == '__main__':
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)

        __tablename__ = 'states'
        id = Column(Integer, unique=True, nullable=False, primary_key=True)
        name = Column(String(128), nullable=False)
