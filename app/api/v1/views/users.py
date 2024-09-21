#!/usr/bin/python3
"""Customer views """

from app.api.v1.views import app_views
from app.models.customers import Customer
from app.models import storage
from flask import abort, jsonify, make_response, request
from app.models.order import Order


@app_views.route('/customer', methods=['GET'],
                 strict_slashes=False)
def list_customer():
    """List customer """

    list_of_user = []
    customer = storage.all(Customer)

    if list_of_user is None:
        abort(404, description='Not found')

    for values in customer.values():
        list_of_user.append(values.to_dict())

    response = make_response(jsonify(list_of_user), 200)
    return response


@app_views.route('/customer/<customer_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(customer_id):
    """Gets a particular user object """

    customer = storage.get(Customer, customer_id)
    if customer is None:
        abort(404, description='Customer Not found')

    response = make_response(jsonify(Customer.to_dict()), 200)
    return response


@app_views.route('/customers', methods=['POST'], strict_slashes=False)
def create_Customer():
    """creates Customer through api route"""

    data = request.get_json()
    if data is None:
        abort(400, description='Not a json')

    required_args = ['name', 'password', 'email', 'address']

    for args in required_args:
        if args not in data:
            abort(400, description=f'{args} is required')

    new_customer = Customer()

    for key, value in data.items():
        if key == 'password':
            new_customer.set_password(value)
            continue
        setattr(new_customer, key, value)

    try:
        storage.new(new_customer)
        storage.save()
    except Exception as e:
        print(f"Error: {e}")
        abort(500, description="Error while saving\
            customersto the database")

    response = make_response(jsonify(new_customer.to_dict()), 201)
    return response


@app_views.route('/customers/<customer_id>/<order_id>',
                 methods=['GET', 'PUT'], strict_slashes=False)

def get_customersorders(customer_id, order_id):
    """Gets aparticular customers order
    by customersid and order_id

    also updates a customersand append an order to an exiciting customers    """

    if request.method == 'GET':
        customers = storage.get(Customer, customer_id)
    
        if customer is None:
            abort(400, description='customer Not found')

        customer_order = next((u for u in customer.orders
                           if u.id == order_id), None)

        response = make_response(jsonify(customer_order.to_dict()), 200)
        return response

    elif request.method == 'PUT':
        customer = storage.get(Customer, customer_id)

        if Customer is None:
            abort(400, description='Customer Not found')

        order = storage.get(Order, order_id)
        if order is None:
            abort(404, description='Order not found')

        if order not in Customer.orders:
            Customer.orders.append(order)
            try:
                storage.save()
            except Exception as e:
                print(f"Error: {e}")
                abort(500, description="Error while saving\
                      changes to the database")

        response = make_response(jsonify(Customer.to_dict()), 200)
        return response


@app_views.route('/customers/<customer_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_Customer(customer_id):
    """Deletes a particular Customer """

    customer_to_delete = storage.get(Customer, customer_id)
    if customer_to_delete is None:
        abort(404, description='Customer not found')

    try:
        storage.delete(customer_to_delete)
        storage.save()
    except Exception as e:
        print(f'Error {e}')
        abort(500, description='an error occured while\
              trying to delete the Customer')

    response = make_response(jsonify({}), 200)
    return response
