#!/usr/bin/python3
"""Registers route for registering user """

from flask import Blueprint, url_for, redirect, flash, render_template
from app.models.registration_form import RegisterationForm
from flask_login import current_user
from app.models.user import User

register_user = Blueprint('register_user', __name__,
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
        user = User(
            name=form.username.data,
            email=form.email.data,
            address=form.address.data
        )

        user.set_password(form.password.data)
        try:
            storage.new(user)
            storage.save()
        except Exception as e:
            print(f'{e} error occured while trying to commit to database')

        flash('Congratulations, you are now a registered user!')

        return redirect(url_for('login_view.login_route'))
    
    return render_template('register.html', form=form)


