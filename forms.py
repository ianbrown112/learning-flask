from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
class SignupForm(FlaskForm):
	first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
	email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter a valid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Password must be at least 6 characters long.")])
	submit = SubmitField('Sign up', validators=[DataRequired()])