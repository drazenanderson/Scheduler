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
	status = SelectField('status', choices=[('customer', 'Customer'), ('client', 'Client')], validators=[DataRequired()])


class WindowForm(Form):
	day = StringField('day')
	first = BooleanField('first')
	second = BooleanField('second')
	third = BooleanField('third')
	fourth = BooleanField('fourth')
	fifth = BooleanField('fifth')
	sixth = BooleanField('sixth')
	seventh = BooleanField('seventh')
	eighth = BooleanField('eighth')
	ninth = BooleanField('ninth')
	tenth = BooleanField('tenth')
	eleventh = BooleanField('eleventh')
	twelfth = BooleanField('twelfth')
	thirteenth = BooleanField('thirteenth')
	fourteenth = BooleanField('fourteenth')
	fifteenth = BooleanField('fifteenth')
	sixteenth = BooleanField('sixteenth')