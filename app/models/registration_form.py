#!/usr/bin/python3
"""Registeration form for users"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import ValidationError, EqualTo, Email, DataRequired
from app.models import storage
from app.models.user import User
from flask import flash


class RegisterationForm(FlaskForm):
    """Registration class form """

    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('repeat password', validators=[DataRequired(), EqualTo('password')])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Register')


    def validate_username(self, username):
        """checks if username is already in database"""

        user = next((user for user in storage.all(User).values() if user.name == username), None)
        if user is not None:
            raise ValidationError('Please use a different username.')
        
    def validate_email(self, email):
        """checks if email already exists in the database"""

        user = next((user for user in storage.all(User).values() if user.email == email ), None)

        if user is not None:
            raise ValidationError('Please use a different email address')
        