#!/usr/bin/python3

from models.user import User
from models.order import Order
from models.supply import Supply
from models.product import Product
from models import storage


# new_product = Product(name='Ice_fish', description='Abakiliki rice', price=1500.00, stock_quantity=30)
# supply_product = Supply(name='first supplier', address='No 51 Iweka Road', price=5000)

# supply_product.products.append(new_product)

# storage.new(supply_product)
# storage.new(new_product)
# storage.save()



print(storage.all('product'))





