#!/usr/bin/python3
"""product order table"""

from sqlalchemy import Table, ForeignKey, Column, String
from app.models.basemodel import Base
from sqlalchemy.orm import relationship


class ProductOrder(Base):
    """Association class with Product and Order"""
    
    __tablename__ = 'product_orders'

    product_id = Column(String(60), ForeignKey('products.id'), primary_key=True)
    order_id = Column(String(60), ForeignKey('orders.id'), primary_key=True)

    product = relationship('Product', back_populates='product_orders')
    orders = relationship('Order', back_populates='order_products')
