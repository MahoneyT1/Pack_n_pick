#!/usr/bin/python3

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class postProductForm(FlaskForm):
    """post product form"""

    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    stock_quantity = IntegerField('stock_quantity', validators=[DataRequired()], default=0)
    price = IntegerField('price', validators=[DataRequired()], default=0)
    submit = SubmitField('Post product')
