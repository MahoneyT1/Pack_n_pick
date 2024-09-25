#!/usr/bin/python3
"""Ading product to cart"""

from flask import Blueprint, flash, redirect, url_for,render_template
#from app import login
from flask_login import login_required, current_user
from app.models.forms.form import AddProductForm
from app.models.customers import Customer
from app.models import storage
from app.models.cart import Cart
from app.models.product import Product
from app.models.cart_product import CartProduct


views = Blueprint('views', __name__, static_folder='../static', template_folder='../templates')


@views.route('/add-to-cart', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def addToCart():
    """adds producs to cart"""

    form = AddProductForm()
    customer_id = current_user.id

    if form.validate_on_submit():
        product_id = form.product_id.data
        quantity = int(form.quantity.data)

        # find the customer with id

        customer = storage.get(Customer, customer_id)

        if customer is None:
            flash('Customer not found')
            return redirect(url_for('home_page_view.home'))
        
        cart = customer.cart
        if cart is None:
            print(customer_id, "this is customer id **************")
            cart = Cart(customer_id=customer.id, quantity=quantity)
            storage.new(cart)
            storage.save()

        # find the product to add to cart
        product = storage.get(Product, product_id)
        if product is None:
            flash("product not found")
            return redirect(url_for('views.addToCart'))

        session = storage.get_session()

        cart_product = session.query(CartProduct).filter_by(cart_id=cart.id,
                                                                      product_id=product.id,
                                                                      quantity=quantity).first()
        print(cart_product)

        if cart_product:
            cart_product.quantity += quantity
        else:
            new_cart_product = CartProduct(cart_id=cart.id, product_id=product.id, quantity=int(quantity))

            storage.new(new_cart_product)
            storage.save()
            flash('successfully added to cart')
        return redirect(url_for('views.addToCart'))
    
    return render_template('add_productcart.html', form=form)


@views.route('/carts', methods=['GET'], strict_slashes=False)
def view_carts():

    customer_id = current_user

    customer = storage.get(Customer, customer_id)
    if customer is None:
        flash('your cart is empty')
        return redirect(url_for('views.view_carts'))

    cart = customer.cart_item

    cart_item = storage.get(CartProduct, cart.id)
    return render_template('cart.html', cart=cart_item)
    