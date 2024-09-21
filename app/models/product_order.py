#!/usr/bin/python3
"""product order table"""

from sqlalchemy import Table, ForeignKey, Column, String
from app.models.basemodel import Base

product_order = Table(
    'product_order',
    Base.metadata,
    Column('products_order_id', String(60), ForeignKey('products.id'), primary_key=True),
    Column('orders_product_id', String(60), ForeignKey('orders.id'), primary_key=True)
    )