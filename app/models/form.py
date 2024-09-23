#!/usr/bin/python3
"""This files handles the form login class"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from werkzeug.datastructures import MultiDict
#from api.v1.app import app


class LoginForm(FlaskForm):
    """app login form"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit =SubmitField('Sign in')


class AddProductForm(FlaskForm):
    """form for adding product to cart"""

    product_id = StringField('product_id', validators=[DataRequired()])
    quantity = IntegerField('quantity', validators=[DataRequired()], default=1)
    submit = SubmitField('Add to cart')