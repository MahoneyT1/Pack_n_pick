from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from app.models.form import LoginForm
from flask_login import current_user, login_user
from app.models import storage
from app.models.user import User


# created a blueprint solely for login route
login_view = Blueprint('login_view', __name__,
                       static_folder='static',
                        template_folder='../templates',
                         url_prefix='/')


@login_view.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login_route():
    """"Login route manages and renders loin template"""
    from .homepage import home_page_view


    form = LoginForm()

    if current_user.is_authenticated:
        return render_template('homepage.html')
    
    if form.validate_on_submit():
        user = next((user for user in storage.all(User).values()
                     if user.name == form.username.data), None)

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login_view.login_route'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home_page_view.home'))

    return render_template('login.html', title='Sign in', form=form)
