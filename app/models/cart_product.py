#!/usr/bin/python3
"""cart and product association table"""

from sqlalchemy import ForeignKey, Column, Integer, String
from app.models.basemodel import Base
from sqlalchemy.orm import relationship


class cartProduct(Base):
    """relationship of cart and product"""

    __tablename__ = 'cart_products'

    cart_id = Column(String(60), ForeignKey('carts.id'), primary_key=True)
    product_id = Column(String(60), ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)


    # relationship many to many
    cart = relationship('Cart', back_populates='cart_products')
    product = relationship('Product', back_populates='product_carts')