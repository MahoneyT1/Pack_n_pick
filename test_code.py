#!/usr/bin/python3

from models.user import User
from models.order import Order
from models.supply import Supply
from models.product import Product
from models import storage
from models import association_supply_product


product = Product(
    name='garri',
    description='ijebu ode main market',
    stock_quantity=3,
    price=500.3
)

suppler1 = Supply(
    name='ignatus',
    address='iweka road onitsha',
    price=300
)

product.suppliers.append(suppler1)
storage.new(product)
storage.new(suppler1)
storage.save()