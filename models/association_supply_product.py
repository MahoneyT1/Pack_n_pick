#!/bin/python3
"""Association table for suppliers and products"""

from sqlalchemy import Table, Column, String, ForeignKey
from models.basemodel import Base


supplier_product = Table(
    'supplier_product', Base.metadata,
    Column('supplier_id', String(60),
           ForeignKey('suppliers.id'), primary_key=True),
    Column('product_id', String(60),
           ForeignKey('products.id'), primary_key=True)   
)
