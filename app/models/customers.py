#!/usr/bin/python3
""" User model """

from app.models.basemodel import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
# from app.models.cart import Cart


class Customer(UserMixin, BaseModel, Base):
    """User class"""

    __tablename__ = 'customers'

    id = Column(String(60),primary_key=True, unique=True, nullable=False)
    name = Column(String(60), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(300), unique=True, nullable=False)
    address = Column(String(200), nullable=False)

    # relationship with order one user to many orders
    orders = relationship(
        'Order', backref='customer', cascade='all, delete-orphan')

    products = relationship('Product', back_populates='customer', cascade='all, delete-orphan')

    # one to one relationship with cart
    cart = relationship('Cart', uselist=False, back_populates='customers', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'email' in kwargs:
            self.email = kwargs['email']
        if 'address' in kwargs:
            self.address = kwargs['address']
        if 'password' in kwargs:
            self.set_password(kwargs['password'])

    def set_password(self, password):
        """Sets flask password"""
        self.password = generate_password_hash(password=password)

    def check_password(self, password):
        """Checks if password is correct"""
        return check_password_hash(self.password, password)
    
    def order(self):
        """Returns a list of user orders"""
        return self.orders
    
    def __repl__(self):
        return f'{self.__class__.__name__} {self.id} {self.__dict__}'
    
