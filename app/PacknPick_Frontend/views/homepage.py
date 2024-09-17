from models.form import LoginForm
from models import storage
from flask_login import current_user, login_user
from . import app
from flask import request, render_template, url_for, redirect

@app.route('/homepage', methods=['GET'], strict_slashes=False)
def homepage():
    return render_template('homepage.html')
