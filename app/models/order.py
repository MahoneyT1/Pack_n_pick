#!/usr/bin/python3
""" order model """

from app.models.basemodel import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.models.customers import Customer
from app.models.product import Product
from app.models.product_order import product_order

class Order(BaseModel, Base):
    """representaton of order table"""

    __tablename__ = 'orders'

    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    quantity = Column(Integer, nullable=False)
    payment_status = Column(Boolean, default=False, nullable=False)

    # Many to one relationship with user. one user many orders
    customer_id = Column(String(60), ForeignKey('customers.id'), nullable=False)

    # many to many relatonship with products
    products_id = relationship('Product', secondary=product_order, back_populates='orders')



    def __init__(self, *args, **kwargs):
        """initialize order instances """
        super().__init__(self, *args, **kwargs)

        if 'quantity' in kwargs:
            self.quantity = kwargs['quantity']

        if 'payment_status' in kwargs:
            self.paid = kwargs['paid']
        
        if 'customer_id' in kwargs:
            self.customer_id = kwargs['customer_id']

        if 'name' in kwargs:
            self.name = kwargs['name']

    def __repl__(self):
        return f'{self.__class__.__name__} {self.id}'

    def to_dict_order(self):
        return{
            'id': self.id,
            'name': self.name,
            'paid': self.paid,
            'quantity': self.quantity,
            'customer_id': self.customer_id
        }
    
    