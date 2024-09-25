#!/usr/bin/python3
"""Class storage to manage storing data"""

from app.models.basemodel import Base 
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
import os
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError




class DBStorage:
    """Class storage representation """
    from app.models.association_supply_product import supplierProduct
    from app.models.order import Order
    from app.models.product import Product
    from app.models.supply import Supply
    from app.models.customers import Customer
    from app.models.cart_product import CartProduct
    from app.models.product_order import ProductOrder
    from app.models.cart import Cart

    all_class = {
        'order': Order, 'product': Product, 'supply': Supply,
        'customer': Customer, 'supplier_product': supplierProduct,
        'cart_product': CartProduct, 'product_order': ProductOrder,
        'cart': Cart
    }

    __engine = None
    __session = None
    Base = Base

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

    def get_engine(self):
        return self.__engine

    def get_session(self):
        return self.__session()

    def all(self, cls=None):
        """List all data in storage"""
        new_dict = {}
        all_cls = []

        if cls:
            # Query all objects of a specific class
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj  # Ensure object is converted to dict
            return new_dict
        else:
            # Query all objects from all classes
            for cls in self.all_class.values():  # Loop through all registered classes
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj # Ensure each object is converted to dict
            return new_dict

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

    def get(self, cls, id):
        """Gets obj by id"""
        cls_extracted_obj = {}

        try:
            if isinstance(cls, str):
                cls = self.all_class[cls]
            
            if cls and id:
                cls_extracted = self.__session.query(cls).filter_by(id=id).first()

                return cls_extracted
            return None
        except SQLAlchemyError as e:
            print(f"Error retrieving {cls} with id {id}: {e}")
            return None
        
    def delete(self, cls):
        """deletes an instance from the database"""
        try:
            self.__session.delete(cls)
        except SQLAlchemyError as e:
            print({e})
            self.__session.rollback()

    def reload(self):
        """reload save data in memory"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)




        

        

