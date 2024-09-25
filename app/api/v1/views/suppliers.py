#!/usr/bin/python3
"""suppliers route"""

from app.api.v1.views import app_views
from flask import jsonify, make_response, abort, request
from app.models.product import Product
from app.models import storage
from app.models import association_supply_product
from app.models.supply import Supply
from datetime import datetime


@app_views.route('/suppliers', methods=['GET'],
                 strict_slashes=False)
def list_suppler():
    """List suppliers """

    list_of_suppliers = []

    suppliers = storage.all(Supply)
    if list_of_suppliers is None:
        abort(404, description='Supplier not found')

    for supplier in suppliers.values():
        list_of_suppliers.append(supplier.to_dict())

    response = make_response(jsonify(list_of_suppliers), 200)
    return response


@app_views.route('/suppliers/<supplier_id>',
                 methods=['GET'], strict_slashes=False)
def get_supplier(supplier_id):
    """route that fetches a supplier by id"""

    supplier = storage.get(Supply, supplier_id)
    if supplier is None:
        abort(404, description='Supplier Not found')

    response = make_response(jsonify(supplier.to_dict()), 200)
    return response


@app_views.route('/suppliers', methods=['POST'],
                 strict_slashes=False)
def post_supplier():
    """posts a supplier """

    data = request.get_json()
    if data is None:
        abort(400, description='Not a json')

    required_args = ['name', 'address', 'price']

    # create a product instance
    new_supply = Supply()

    for arg in required_args:
        if arg not in data:
            abort(400, description=f'{arg} is required')

    for key, value in data.items():
        setattr(new_supply, key, value)

    storage.new(new_supply)
    storage.save()

    response = make_response(jsonify(new_supply.to_dict()), 200)
    return response


@app_views.route('/suppliers/<supplier_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_supplier(supplier_id):
    """Deletes a supplier by id"""

    supplier_to_delete = storage.get(Supply, supplier_id)
    if supplier_to_delete is None:
        abort(404, description='Not found')

    storage.delete(supplier_to_delete)
    storage.save()

    return make_response(jsonify({}), 201)


@app_views.route('/suppliers/<supplier_id>',
                 methods=['PUT'], strict_slashes=False)
def update_supplier(supplier_id):
    """updates a supplier by id"""

    data = request.get_json()
    if data is None:
        abort(400, description='Not a json')

    supplier = storage.get(Supply, supplier_id)
    if supplier is None:
        abort(404, description='supplier not found')

    cannot_update_arg = ['id', 'created_at']
    for key, value in data.items():
        if key not in cannot_update_arg:
            setattr(supplier, key, value)

    supplier.updated_at = datetime.utcnow()
    try:
        storage.save()
    except Exception as e:
        print(f'Error {e} occured while trying to commit to storage')
        abort(500, description='Error occured')

    response = make_response(jsonify(supplier.to_dict()), 200)
    return response


@app_views.route('/suppliers/<supplier_id>/products',
                 methods=['GET'], strict_slashes=False)
def supplier_product_list(supplier_id):
    """List a post from supplier relationship"""

    supplier = storage.get(Supply, supplier_id)
    if supplier is None:
        abort(404, description='Supplier Not found')

    product = storage.get(Supply)
    if product is None:
        abort(404, description='product Not found')

    products_list = [pro.to_dict() for pro in supplier.products]

    response = make_response(jsonify(products_list), 200)
    return response


# associate an exisiting product to a supplier.products
@app_views.route('/supplier/<supplier_id>/products/<product_id>',
                 methods=['PUT'], strict_slashes=False)
def append_product_to_supplier(supplier_id, product_id):
    """Associates an exisiting product to an exisiting supplier"""

    supplier = storage.get(Supply, supplier_id)
    if supplier is None:
        abort(404, description='Supplier Not found')

    product = storage.get(Product, product_id)
    if product is None:
        abort(404, description='Product Not found')

    if product not in supplier.products:
        supplier.product.append(product)

        # update the datetime
        supplier.updated_at = datetime.utcnow()
        storage.save()

    response = make_response(jsonify(supplier.to_dict()), 200)
    return response
