#!/usr/bin/python3
"""cart and product association table"""

from sqlalchemy import Table, ForeignKey, Column, Integer, String
from app.models.basemodel import Base

cart_product = Table(
    'cart_products', Base.metadata,
    Column('cart_id', String(60), ForeignKey('carts.id'), primary_key=True),
    Column('product_id', String(60), ForeignKey('products.id'), primary_key=True),
    Column('quantity', Integer)
)