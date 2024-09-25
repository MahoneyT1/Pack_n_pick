# #!/usr/bin/python3

from app.models.customers import Customer
from app.models.order import Order
from app.models.supply import Supply
from app.models.product import Product
from app.models import storage
from app.models import association_supply_product
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



cart = Cart(
    customer_id = '120ea274-daa3-4f87-b3f8-68f982a58d9f',
    quantity=3
    )
storage.new(cart)
storage.save()

print(cart)


# storage.new(user1)
# # storage.new(suppler1)
# storage.save()

