#!/usr/bin/python3
"""File product that handles every thing related to product
"""

from app.models.basemodel import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from app.models.association_supply_product import supplier_product
from app.models.product_order import product_order
from app.models.cart_product import cart_product
from app.models.cart import Cart


class Product(BaseModel, Base):
    __tablename__ = 'products'

    id = Column(String(60), primary_key=True, unique=True,
                nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(225), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    suppliers = relationship('Supply', secondary=supplier_product,
                             back_populates='products')
    
    customer_id = relationship('Customer', ForeignKey('customers.id'), back_populates='product')

    # many to many relationship with order
    orders_id = relationship('Order', secondary=product_order, back_populates='product')

    # many to many relationship with cart
    cart_id = relationship('Cart', secondary=cart_product, back_populates='product')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs:
            for key, value in kwargs.items():
                if key in ['name', 'description', 'price', 'stock_quantity']:
                    setattr(self, key, value)
