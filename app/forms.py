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


class WindowForm(Form):
	day = IntegerField('day')
	first = BooleanField('first', default=False)
	second = BooleanField('second', default=False)
	third = BooleanField('third', default=False)
	fourth = BooleanField('fourth', default=False)
	fifth = BooleanField('fifth', default=False)
	sixth = BooleanField('sixth', default=False)
	seventh = BooleanField('seventh', default=False)
	eighth = BooleanField('eighth', default=False)
	ninth = BooleanField('ninth', default=False)
	tenth = BooleanField('tenth', default=False)
	eleventh = BooleanField('eleventh', default=False)
	twelfth = BooleanField('twelfth', default=False)
	thirteenth = BooleanField('thirteenth', default=False)
	fourteenth = BooleanField('fourteenth', default=False)
	fifteenth = BooleanField('fifteenth', default=False)
	sixteenth = BooleanField('sixteenth', default=False)
	status = BooleanField('status', default=False)