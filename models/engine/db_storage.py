#!/usr/bin/python3
""" Module for Handling the database storage """
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City


class DBStorage:
    '''
    For the database engine
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        creation of the engine
        '''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def close(self):
        ''' For closing the storage engine. '''
        self.__session.close()

    def all(self, cls=None):
        '''
        For querying the current database
        '''
        classes = {
            "City": City, "State": State,
            "User": User, "Place": Place,
            "Review": Review
        }
        res = {}
        qrows = []

        if cls:
            '''Quering for all objects that belongs to cls'''
            if type(cls) is str:
                cls = eval(cls)
            qrows = self.__session.query(cls)
            for obj in qrows:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                res[key] = obj
            return res
        else:
            '''Quering for all types of objects'''
            for n, val in classes.items():
                # n for name and val for value
                qrows = self.__session.query(val)
                for obj in qrows:
                    key = '{}.{}'.format(n, obj.id)
                    res[key] = obj
            return res

    def new(self, obj):
        '''for adding the object to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''for commiting all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        ''' for deleting obj from the current database session'''
        self.__session.delete(obj)

    def reload(self):
        '''for creating all tables in the database and for creating
        the current database session from the engine
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        "" "For closing tht session"""
        self.__session.close()
