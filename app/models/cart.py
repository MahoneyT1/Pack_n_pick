#!/usr/bin/python3
""" cart model"""

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.models.cart_product import cart_product
from app.models.basemodel import Base, BaseModel

class Cart(BaseModel, Base):
    """representation of carting system"""
    from app.models.customers import Customer

    __tablename__ = 'carts'

    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    quanity = Column(Integer, nullable=False)

    customer_id = Column(String(60), ForeignKey('customers.id'), nullable=False)

    customer = relationship('Customer', backref='cart')

    # many to many relationship with product
    product_id = relationship('Product', secondary=cart_product, back_populates='cart')
