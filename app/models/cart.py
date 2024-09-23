#!/usr/bin/python3
""" cart model"""

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from app.models.cart_product import cartProduct
from app.models.basemodel import Base, BaseModel


class Cart(BaseModel, Base):
    """representation of carting system"""

    from app.models.customers import Customer

    __tablename__ = 'carts'

    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    quantity = Column(Integer, nullable=False)

    # relationship with customer
    customer_id = Column(String(60), ForeignKey('customers.id'), nullable=False)
    customers = relationship('Customer', back_populates='cart')

    # many to many relationship with product
    cart_products = relationship('cartProduct', back_populates='cart')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'quantity' in kwargs:
            self.quantity = kwargs['quantity']

