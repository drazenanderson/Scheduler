from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SelectField, PasswordField, IntegerField, validators
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)


class UserForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired()])
	first = StringField('first', validators=[DataRequired()])
	last = StringField('last', validators=[DataRequired()])
	phone = StringField('phone', validators=[DataRequired()])


	