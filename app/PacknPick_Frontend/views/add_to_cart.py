#!/usr/bin/python3
"""Ading product to cart"""

from flask import Blueprint, flash, redirect, url_for,render_template
#from app import login
from flask_login import login_required, current_user
from app.models.form import AddProductForm
from app.models.customers import Customer
from app.models import storage
from app.models.cart import Cart
from app.models.product import Product
from app.models.cart_product import cartProduct


views = Blueprint('views', __name__, static_folder='../static', template_folder='../templates')


@views.route('/add-to-cart', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def addToCart():
    """adds producs to cart"""

    form = AddProductForm()
    customer_id = current_user.id 

    if form.validate_on_submit():
        print(f"Product ID: {form.product_id.data}, Quantity: {form.quantity.data}")
        product_id = form.product_id.data
        quantity = int(form.quantity.data)

        # find the customer with id

        customer = storage.get(Customer, customer_id)

        if customer is None:
            flash('Customer not found')
            return redirect(url_for('home_page_view.home'))
        
        cart = customer.cart
        if cart is None:
            cart = Cart(customer_id=customer_id)
            storage.new(cart)

        # find the product to add to cart
        product = storage.get(Product, product_id)
        if product is None:
            flash("product not found")
            return redirect(url_for('home_page_view.home'))
        
        cart_product = storage.__session.query(cartProduct).filter_by(cart_id=cart.id, product_id=product.id).first()

        if cart_product:
            cart_product.quantity += quantity
        else:
            new_cart_product = cartProduct(cart_id=cart.id, product_id=product.id, quantity=int(quantity))

            storage.new(new_cart_product)

        storage.save()
        return redirect(url_for('home_page_view.home'))
    
    return render_template('add_productcart.html', form=form)


@views.route('/carts', methods=['GET'], strict_slashes=False)
def view_carts():

    customer_id = current_user

    customer = storage.get(Customer, customer_id)
    if customer is None:
        flash('your cart is empty')
        return redirect(url_for('views.view_carts'))

    cart = customer.cart_item

    cart_item = storage.get(cartProduct, cart.id)
    return render_template('cart.html', cart=cart_item)
    