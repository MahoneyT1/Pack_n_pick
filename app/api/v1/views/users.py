#!/usr/bin/python3
"""user views """

from app.api.v1.views import app_views
from app.models.user import User
from app.models import storage
from flask import abort, jsonify, make_response, request
from app.models.order import Order


@app_views.route('/users', methods=['GET'],
                 strict_slashes=False)
def list_users():
    """List users """

    list_of_user = []
    users = storage.all(User)

    if list_of_user is None:
        abort(404, description='Not found')

    for values in users.values():
        list_of_user.append(values.to_dict())

    response = make_response(jsonify(list_of_user), 200)
    return response


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(user_id):
    """Gets a particular user object """

    user = storage.get(User, user_id)
    if user is None:
        abort(404, description='User Not found')

    response = make_response(jsonify(user.to_dict()), 200)
    return response


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """creates user through api route"""

    data = request.get_json()
    if data is None:
        abort(400, description='Not a json')

    required_args = ['name', 'password', 'email', 'address']

    for args in required_args:
        if args not in data:
            abort(400, description=f'{args} is required')

    new_user = User()

    for key, value in data.items():
        if key == 'password':
            new_user.set_password(value)
            continue
        setattr(new_user, key, value)

    try:
        storage.new(new_user)
        storage.save()
    except Exception as e:
        print(f"Error: {e}")
        abort(500, description="Error while saving\
            user to the database")

    response = make_response(jsonify(new_user.to_dict()), 201)
    return response


@app_views.route('/users/<user_id>/<order_id>',
                 methods=['GET', 'PUT'], strict_slashes=False)
def get_user_orders(user_id, order_id):
    """Gets aparticular user's order
    by user_id and order_id

    also updates a user and append an order to an exiciting user
    """

    if request.method == 'GET':
        user = storage.get(User, user_id)
        if user is None:
            abort(400, description='User Not found')

        user_order = next((u for u in user.orders
                           if u.id == order_id), None)

        response = make_response(jsonify(user_order.to_dict()), 200)
        return response

    elif request.method == 'PUT':
        user = storage.get(User, user_id)
        if user is None:
            abort(400, description='User Not found')

        order = storage.get(Order, order_id)
        if order is None:
            abort(404, description='Order not found')

        if order not in user.orders:
            user.orders.append(order)
            try:
                storage.save()
            except Exception as e:
                print(f"Error: {e}")
                abort(500, description="Error while saving\
                      changes to the database")

        response = make_response(jsonify(user.to_dict()), 200)
        return response


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """Deletes a particular user """

    user_to_delete = storage.get(User, user_id)
    if user_to_delete is None:
        abort(404, description='User not found')

    try:
        storage.delete(user_to_delete)
        storage.save()
    except Exception as e:
        print(f'Error {e}')
        abort(500, description='an error occured while\
              trying to delete the User')

    response = make_response(jsonify({}), 200)
    return response
