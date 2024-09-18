from app.models.form import LoginForm
from app.models import storage
from flask_login import current_user, login_user, login_required
from .login import login_view
from flask import request, render_template, url_for, redirect, Blueprint
# from app import login


home_page_view = Blueprint('home_page_view', __name__, static_folder='static', template_folder='../templates')

@home_page_view.route('/homepage', methods=['GET'], strict_slashes=False)
@login_required
def home():
    return render_template('homepage.html')
