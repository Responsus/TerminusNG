from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Login form to access writing and settings pages"""

    username = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])