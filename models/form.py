#!/usr/bin/python3
"""This files handles the form login class"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.datastructures import MultiDict
from api.v1.app import app


class LoginForm(FlaskForm):
    """app login form"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit =SubmitField('Sign in')


with app.app_context():

    form_data = MultiDict({
        'username': 'ifeco1234',
        'password': '4444',
        'remember_me': True
        })

    form = LoginForm(form_data)

    if form.validate():
        print('form is validated')
        print('username', form.username.data)
        print('password', form.password.data)
        print('remember_me', form.remember_me.data)