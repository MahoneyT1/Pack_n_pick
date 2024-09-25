#!/usr/bin/python3
"""Logout route"""


from flask_login import logout_user
from .login import login_view
from flask import redirect,url_for, Blueprint


# Blueprint for logout route
logout_view = Blueprint('logout_view', __name__,
                        template_folder='../templates',
                        static_folder='../static')


@logout_view.route('/logout', strict_slashes=False)
def logout():
    logout_user()
    return redirect(url_for('login_view.login_route'))
