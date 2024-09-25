#!/usr/bin/python3
"""File product that handles everything related to product
"""

from app.models.basemodel import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from app.models.association_supply_product import supplierProduct
from app.models.product_order import ProductOrder
from app.models.cart_product import CartProduct
from app.models.cart import Cart

class Product(BaseModel, Base):
    __tablename__ = 'products'

    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(225), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    
    # Define customer_id as a foreign key
    customer_id = Column(String(60), ForeignKey('customers.id'))

    # Relationship with customer
    customer = relationship('Customer', back_populates='products')

    # Relationship with supplier (Supply)
    product_suppliers = relationship('supplierProduct', back_populates='product')
    
    # Many-to-many relationship with order
    product_orders = relationship('ProductOrder', back_populates='product')

    # Many-to-many relationship with cart
    product_carts = relationship('CartProduct', back_populates='product')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs:
            for key, value in kwargs.items():
                if key in ['name', 'description', 'price', 'stock_quantity']:
                    setattr(self, key, value)
