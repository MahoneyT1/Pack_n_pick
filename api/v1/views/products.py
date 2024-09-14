#!/usr/bin/python3
"""Products route"""

from api.v1.views import app_views
from flask import jsonify, make_response, abort, request
from models.product import Product
from models import storage
from models import association_supply_product
from models.supply import Supply
from datetime import datetime


@app_views.route('/products', methods=['GET'],
                 strict_slashes=False)
def list_product():
    """List products """

    list_of_product = []

    products = storage.all(Product)
    if list_of_product is None:
        abort(404, description='Product not found')

    for product in products.values():
        list_of_product.append(product.to_dict())

    response = make_response(jsonify(list_of_product), 200)
    return response


@app_views.route('/products/<product_id>',
                 methods=['GET'], strict_slashes=False)
def get_product(product_id):
    """route that fetches a product by id"""

    product = storage.get(Product, product_id)
    if product is None:
        abort(404, description='Product Not found')

    response = make_response(jsonify(product.to_dict()), 200)
    return response


@app_views.route('/products', methods=['POST'],
                 strict_slashes=False)
def post_product():
    """posts a product """

    data = request.get_json()
    if data is None:
        abort(400, description='Not a json')

    required_args = ['name', 'description',
                     'stock_quantity', 'price']

    # create a product instance
    new_product = Product()

    for arg in required_args:
        if arg not in data:
            abort(400, description=f'{arg} is required')

    for key, value in data.items():
        setattr(new_product, key, value)

    storage.new(new_product)
    storage.save()

    response = make_response(jsonify(new_product.to_dict()), 200)
    return response


@app_views.route('/products/<product_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_product(product_id):
    """Deletes a product"""

    product_to_delete = storage.get(Product, product_id)
    if product_to_delete is None:
        abort(404, description='Not found')

    storage.delete(product_to_delete)
    storage.save()

    return make_response(jsonify({}), 201)


@app_views.route('/products/<product_id>',
                 methods=['PUT'], strict_slashes=False)
def update_product(product_id):
    """updates a product by id"""

    data = request.get_json()
    if data is None:
        abort(400, description='Not a json')

    product = storage.get(Product, product_id)
    if product is None:
        abort(404, description='Product not found')

    cannot_update_arg = ['id', 'created_at']
    for key, value in data.items():
        if key not in cannot_update_arg:
            setattr(product, key, value)

    # update updated_at time
    product.updated_at = datetime.utcnow()

    try:
        storage.save()
    except Exception as e:
        print(f'Error {e} occured while trying to commit to storage')
        abort(500, description='Error occured')

    response = make_response(jsonify(product.to_dict()), 200)
    return response


# create assosiation route for product
@app_views.route('/products/<product_id>/suppliers',
                 methods=['GET'], strict_slashes=False)
def product_suppliers(product_id):
    """List all the suppliers that supplied a product"""

    product = storage.get(Product, product_id)
    if product is None:
        abort(404, description='Product Not found')

    suppliers = [su.to_dict() for su in product.suppliers]

    response = make_response(jsonify(suppliers), 200)
    return response


# route for appending an existing supplier in product.supplier's list
@app_views.route('/products/<product_id>/suppliers/<supplier_id>',
                 methods=['PUT'], strict_slashes=False)
def product_supplier_post(product_id, supplier_id):
    """Posts a supplier and associate it with product"""

    product = storage.get(Product, product_id)
    if product is None:
        abort(404, description='Product Not found')

    supplier = storage.get(Supply, supplier_id)
    if supplier is None:
        abort(404, description='Supplier Not found')

    if supplier not in product.suppliers:
        product.suppliers.append(supplier)

        product.updated_at = datetime.utcnow()
        storage.save()

    response = make_response(jsonify(product.to_dict()), 200)
    return response
