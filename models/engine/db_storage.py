#!/usr/bin/python3
""" Database Storage """
from os import getenv
import models
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {
        'State': State, 'City': City
        }


class DBStorage():
    """ Databasse Storage definition """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialization of the Database Storage """
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    getenv('HBNB_MYSQL_USER', ''),
                    getenv('HBNB_MYSQL_PWD', ''),
                    getenv('HBNB_MYSQL_HOST', ''),
                    getenv('HBNB_MYSQL_DB', '')),
                pool_pre_ping=True)
        if getenv('HBNB_ENV', '') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session all objects
        depending on the class
        Args:
            cls(class): class reference or name
        """
        objs = {}
        if cls is None:
            for key in classes:
                for instance in self.__session.query(classes[key]):
                    new_key = key + '.' + instance.id
                    if '_sa_instance_state' in instance.__dict__:
                        del instance.__dict__['_sa_instance_state']
                    objs[new_key] = instance
        else:
            if cls in classes:
                for instance in self.__session.query(classes[cls]):
                    new_key = cls + '.' + instance.id
                    if '_sa_instance_state' in instance.__dict__:
                        del instance.__dict__['_sa_instance_state']
                    objs[new_key] = instance
        return objs

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()
        # self.__session.close()

    def delete(self, obj=None):
        """ delete from the current database session obj """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
                sessionmaker(
                    bind=self.__engine,
                    expire_on_commit=False))
