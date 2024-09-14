#!/usr/bin/python3
""" View for orders """

from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.order import Order
from models.user import User
from sqlalchemy.exc import SQLAlchemyError


@app_views.route('/orders', methods=['GET'], strict_slashes=False)
def list_of_orders():
    """List of orders """
    all_orders = []

    orders = storage.all(Order)

    if orders is None:
        abort(404, description='Not found')

    for order in orders.values():
        all_orders.append(order.to_dict())

    response = make_response(jsonify(all_orders))
    return response


@app_views.route('/orders/<order_id>', methods=['GET'], strict_slashes=False)
def get_order(order_id):
    """fetches a particular orders """

    order = storage.get(Order, order_id)

    if order is None:
        abort(404, description='Order Not found')

    response = make_response(jsonify(order.to_dict()), 200)
    return response


@app_views.route('/users/<user_id>/orders',
                 methods=['POST'], strict_slashes=False)
def post_user_order(user_id):
    """Post user order """

    datas = request.get_json()

    if datas is None:
        abort(400, description='Not a json')

    # check if user exists
    user = storage.get(User, user_id)
    if user is None:
        abort(404, description='User not found')

    # required attributes
    required_attr = ['name', 'quantity', 'paid']

    for attribute in required_attr:
        if attribute not in datas:
            abort(400, description=f'missing a {attribute} field')

    # create new order and append it to user
    new_order = Order(**datas)
    new_order.user_id = user_id

    # commit the transaction to database
    try:
        storage.new(new_order)
        storage.save()
    except SQLAlchemyError as e:
        print(f'{e} error occured')
        abort(500)

    order_dict = new_order.to_dict()
    response = make_response(jsonify(order_dict), 201)

    return response


@app_views.route('/orders/<order_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_order(order_id):
    """Deletes an order """

    order_to_delete = storage.get(Order, order_id)
    if order_to_delete is None:
        abort(404, description='Not found')

    storage.delete(order_to_delete)
    storage.save()

    response = make_response(jsonify({}), 200)
    return response


@app_views.route('/orders/<order_id>', methods=['PUT'], strict_slashes=False)
def update_order(order_id):
    """updates an order by id"""

    data = request.get_json()
    if data is None:
        abort(400, description='Not a json')

    order_to_update = storage.get(Order, order_id)
    if order_to_update is None:
        abort(404, description='Not found')

    for key, value in data.items():
        setattr(order_to_update, key, value)

    try:
        storage.save()
    except Exception as e:
        print(f'{e}')
    response = make_response(jsonify(order_to_update.to_dict()), 200)
    return response
