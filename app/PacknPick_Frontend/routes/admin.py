#!/usr/bin/python3
"""admin route to handle admin related works"""

from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import login_required
from flask_login import login_required, current_user
from app.models.forms.post_form import postProductForm
from app.models.product import Product
from app.models import storage


admin = Blueprint('admin', __name__, template_folder='../templates', url_prefix='/admin')


@admin.route('/add-products', methods=['POST', 'GET'], strict_slashes=False)
@login_required
def post_product():
    """Post products on the shop """
    
    if current_user.is_authenticated:
        form = postProductForm()

        if form.validate_on_submit():
            name = form.name.data
            price = form.price.data
            description = form.description.data
            stock_quantity = form.stock_quantity.data

            new_product = Product(
                name=name, price=price, description=description,
                stock_quantity=stock_quantity
            )

            try:
                storage.new(new_product)
                storage.save()
                flash('new product succesfully created')
            except Exception as e:
                flash(f'Error {e} occoured')

            return redirect(url_for('admin.post_product'))
    
    return render_template('post_product.html', form=form)


# update a product
@admin.route('/update-products/<product_id>', methods=['POST', 'GET'], strict_slashes=False)
@login_required
def update_product(product_id):
    """updates a product by Id """

    form = postProductForm()

    item_to_update = storage.get(Product, product_id)

    form.name.render_kw = {'placeholder': item_to_update.name }
    form.description.render_kw = {'placeholder': item_to_update.description }
    form.price.render_kw = {'placeholder': item_to_update.price }
    form.stock_quantity.render_kw = {'placeholder': item_to_update.stock_quantity }

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        price = form.price.data
        stock_quantity = form.stock_quantity.data

        