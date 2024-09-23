#!/usr/bin/python3
"""Registers route for registering user """

from flask import Blueprint, url_for, redirect, flash, render_template
from app.models.registration_form import RegisterationForm
from flask_login import current_user
from app.models.customers import Customer

register_user = Blueprint('register_customer', __name__,
                          template_folder='../templates',
                          static_folder='../static')

@register_user.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register_route():
    """method the registers user """

    from app.models import storage

    if current_user.is_authenticated:
        return redirect(url_for('home_page_view.home'))
    
    form = RegisterationForm()

    if form.validate_on_submit():
        customer = Customer(
            name=form.username.data,
            email=form.email.data,
            address=form.address.data
        )

        customer.set_password(form.password.data)
        try:
            storage.new(customer)
            storage.save()
        except Exception as e:
            print(f'{e} error occured while trying to commit to database')

        flash('Congratulations, you are now a registered customer!')

        return redirect(url_for('login_view.login_route'))
    
    return render_template('register.html', form=form)


