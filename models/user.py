#!/usr/bin/python3
""" User model """

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship 


class User(BaseModel, Base):
    """User class"""

    __tablename__ = 'users'

    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(30), nullable=False)
    address = Column(String(100), nullable=False)

    # relationship with order one user to many orders
    orders = relationship(
        'Order', back_populates='user', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'name' in kwargs:
            self.name = kwargs['name']
        if 'email' in kwargs:
            self.email = kwargs['email']
        if 'address' in kwargs:
            self.address = kwargs['address']
        if 'password' in kwargs:
            self.password = kwargs['password']
