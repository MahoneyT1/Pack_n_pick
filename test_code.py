#!/usr/bin/python3

from models.user import User
from models.order import Order
from models.supply import Supply
from models.product import Product
from models import storage

obj_cls = {
    "user": User,
    "order": Order,
    "supply": Supply,
    "product": Product
}

#new_user = User(name='ife-co', email='ifeanyitech@email.com', password='2325', address='isiala mbano')
# new_order = Order(name='orji', paid=True, quantity=500, user_id='5d5bc521-5581-41e1-b911-35d796ddcacd')




#storage.new(new_user)
# storage.new(new_order)
# storage.save()

user_id = '5d5bc521-5581-41e1-b911-35d796ddcacd'

all_user = storage.get(User, user_id)
user1 = []

for user in all_user.orders:
    print(user)

# for user in all_user:
#     for order in user.orders:
#         print(order.to_dict())


# print(list_of_order)





