#!/usr/bin/python3
""" order model """

from app.models.basemodel import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.models.customers import Customer
from app.models.product import Product
from app.models.product_order import ProductOrder  # Use CamelCase for class names

class Order(BaseModel, Base):
    """Representation of order table"""

    __tablename__ = 'orders'

    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    quantity = Column(Integer, nullable=False)
    payment_status = Column(Boolean, default=False, nullable=False)

    # Many to one relationship with user. One user many orders
    customer_id = Column(String(60), ForeignKey('customers.id'), nullable=False)
    customer = relationship('Customer', back_populates='orders')

    # Many to many relationship with products
    order_products = relationship('ProductOrder', back_populates='orders', cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        """Initialize order instances"""
        super().__init__(*args, **kwargs)  # Fixed the constructor call

        if 'quantity' in kwargs:
            self.quantity = kwargs['quantity']

        if 'payment_status' in kwargs:  # Correct the key name
            self.payment_status = kwargs['payment_status']  # Fixed the attribute name

        if 'customer_id' in kwargs:
            self.customer_id = kwargs['customer_id']

        if 'name' in kwargs:
            self.name = kwargs['name']

    def __repr__(self):  # Fixed __repl__ to __repr__
        return f'{self.__class__.__name__} {self.id}'

    def to_dict_order(self):
        return {
            'id': self.id,
            'name': self.name,
            'paid': self.payment_status,  # Fixed to match the actual attribute
            'quantity': self.quantity,
            'customer_id': self.customer_id
        }
