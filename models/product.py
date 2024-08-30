#!/usr/bin/python3
"""File product that handles every thing related to product
"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from models.association_supply_product import supplier_product


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

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        if kwargs:
            for key, value in kwargs.items():
                if key in ['name', 'description', 'price', 'stock_quantity']:
                    setattr(self, key, value)
