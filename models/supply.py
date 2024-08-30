#!/usr/bin/python3
""" supplier model """

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from models.association_supply_product import supplier_product


class Supply(BaseModel, Base):
    """Supplier class """

    __tablename__ = 'suppliers'

    id = Column(String(60), primary_key=True, unique=True,
                nullable=False)
    name = Column(String(100), nullable=False)
    address = Column(String(250), nullable=False)
    price = Column(Float, nullable=False)

    # one to many relationship, one supplier to have many products
    products = relationship('Product', secondary=supplier_product,
                            back_populates='suppliers')

    def __init__(self, *args, **kwargs):
        """initialize new instance with attributes"""
        super().__init__(*args, **kwargs)

        for key, value in kwargs.items():
            if key in ['id', 'name', 'address', 'price']:
                setattr(self, key, value)
