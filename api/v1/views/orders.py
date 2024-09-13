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


@app_views.route('/users/<user_id>/orders', methods=['GET'], strict_slashes=False)
def list_users_order(user_id):
    """lists users orders """

    user = storage.get(User, user_id)
    user_order = []

    if user is None:
        abort(404, description='Not found')

    for order in user.orders:
        user_order.append(order.to_dict())

    response = make_response(jsonify(user_order), 200)
    return response


@app_views.route('/users/<user_id>/orders', methods=['POST'], strict_slashes=False)
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
