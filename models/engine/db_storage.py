#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv, environ
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class is linked to MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """__init__ method"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ), pool_pre_ping=True)
        if environ.get('HBNB_ENV'):
            if getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            the list of objects of one type of class
        """
        if cls:
            objects = self.__session.query(cls).all()
        else:
            all_classes = [Amenity, City, Place, Review, State, User]
            objects = []
            for c in all_classes:
                objects += self.__session.query(c)
        dicti = {}
        for obj in objects:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            dicti[key] = obj
        return dicti

    def new(self, obj):
        """sets __session to given obj
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def delete(self, obj=None):
        """deletes obj from __session"""
        if obj:
            self.__session.delete(obj)

    def save(self):
        """saves db into MySQLdb
        """
        self.__session.commit()

    def reload(self):
        """creates tables in db
        """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """ calls close() """
        self.__session.close()
