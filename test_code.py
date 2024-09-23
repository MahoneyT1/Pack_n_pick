# #!/usr/bin/python3

from app.models.customers import Customer
# from app.models.order import Order
# from app.models.supply import Supply
# from app.models.product import Product
# from app.models import storage
# from app.models import association_supply_product
from app.models.cart import Cart

# # product = Product(
# #     name='garri',
# #     description='ijebu ode main market',
# #     stock_quantity=3,
# #     price=500.3
# # )

# # suppler1 = Supply(
# #     name='ignatus',
# #     address='iweka road onitsha',
# #     price=300
# # )

# # product.suppliers.append(suppler1)

# user1 = User(
#     name='ifeanyi',
#     email='ifeanyi@email.com',
#     password='12345',
#     address='Mbari street'
# )

# storage.new(user1)
# # storage.new(suppler1)
# storage.save()

from sqlalchemy import inspect

cart_mapper = inspect(Cart)
customer_mapper = inspect(Customer)
print(cart_mapper.attrs.keys())
print(customer_mapper.attrs.keys())
