#!/usr/bin/python3
""" order model """

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String, Float, Boolean
from sqlalchemy.orm import relationship
from models.user import User
from models.product import Product


class Order(BaseModel, Base):
    """representaton of order table"""

    __tablename__ = 'orders'

    id = Column(String(60), primary_key=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    paid = Column(Boolean, default=False, nullable=False)

    # Many to one relationship with user. one user many orders
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='orders')

    def __init__(self, *args, **kwargs):
        """initialize order instances """
        super().__init__(self, *args, **kwargs)

        if 'quantity' in kwargs:
            self.quantity = kwargs['quantity']

        if 'paid' in kwargs:
            self.paid = kwargs['paid']
        
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
