from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from app.models.form import LoginForm
from flask_login import current_user, login_user
from app.models import storage
from app.models.user import User


web_service = Blueprint('web_service', __name__,
                        template_folder='templates',
                        static_folder='static',url_prefix='/')


@web_service.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login_route():
    """"Login route manages and renders loin template"""

    form = LoginForm()

    if current_user.is_authenticated:
        return render_template('homepage.html')
    
    if form.validate_on_submit():
        user = storage.__session.query(User).where(User.name == form.username.data)

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect('home')
    
    return render_template('login.html', title='Sign in', form=form)
