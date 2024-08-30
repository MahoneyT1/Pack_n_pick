#!/usr/bin/python3
"""Class storage to manage storing data"""

from models.basemodel import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
import os
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError



class DBStorage:
    """Class storage representation """
    from models.association_supply_product import supplier_product
    from models.order import Order
    from models.product import Product
    from models.supply import Supply
    from models.user import User

    all_class = {
        'order': Order, 'product': Product, 'supply': Supply, 'user': User
    }

    __engine = None
    __session = None

    Base = DeclarativeBase
    def __init__(self):
        """initialize the database connection"""

        connection_string = "mysql+mysqldb://{}:{}@{}:{}/{}".format(
                                                                    os.getenv('MYSQL_USERNAME'),
                                                                    os.getenv('MYSQL_PASSWORD'),
                                                                    os.getenv('MYSQL_HOST'),
                                                                    os.getenv('MYSQL_PORT'),
                                                                    os.getenv('MYSQL_DATABASE')
                                                                    )

        self.__engine = create_engine(connection_string, echo=True, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)

        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """List all data in storage"""

        new_list = []

        if cls is None:
            for key, value in self.all_class.items():
                result_query = self.__session.query(value).all()

                for obj in result_query:
                    new_list.append(obj.to_dict())

            return new_list
        
        cls = self.all_class[cls]

        query_result = self.__session.query(cls).all()
        for obj in query_result:
            new_list.append(obj.to_dict())

        return new_list
        
    def new(self, obj):
        """adds new created class into the database session"""

        try:
            self.__session.add(obj)
        except SQLAlchemyError as e:
            print(f'Error while adding new obj to the database {e}')
            self.__session.rollback()

    def save(self):
        """commits obj in current session to database"""

        try:
            self.__session.commit()
        except SQLAlchemyError as e:
            print(f'Error while trying to commit obj in current session to database {e}')
            self.__session.rollback()

    def get(self, obj):
        """Gets obj by id"""
    def reload(self):
        """reload save data in memory"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)




        

        

