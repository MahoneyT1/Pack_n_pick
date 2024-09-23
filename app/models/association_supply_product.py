#!/bin/python3
"""Association table for suppliers and products"""

from sqlalchemy import Column, String, ForeignKey
from app.models.basemodel import Base
from sqlalchemy.orm import relationship


class supplierProduct(Base):
    """many to many relationship
    An Association class
    """
    __tablename__ = 'supplier_products'
    supplier_id = Column(String(60), ForeignKey('suppliers.id'), primary_key=True)
    product_id = Column(String(60), ForeignKey('products.id'), primary_key=True)

    supplier = relationship('Supply', back_populates='supplier_products')
    product = relationship('Product', back_populates='product_suppliers')

