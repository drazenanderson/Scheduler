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
	
class FrameForm(Form):
	day = StringField('day', validators=[DataRequired()])
	starthour = SelectField('starthour', choices=[(1, '1'), (2, '2'), (3, '3'), 
												  (4, '4'), (5, '5'), (6, '6'), (7, '7'), 
												  (8, '8'), (9, '9'), (10, '10'), (11, '11'), (0, '12')])
										  
	startminutes = SelectField('startminutes', choices=[(0, '00'), (1, '01'), (2, '02'), (3, '03'), (4, '04'),
														(5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), 
													    (10, '10'), (11, '11'), (12, '12'), (13, '13'), 
													    (14, '14'), (15, '15'), (16, '16'), (17, '17'), 
													    (18, '18'), (19, '19'), (20, '20'), (21, '21'), 
													    (22, '22'), (23, '23'), (24, '24'), (25, '25'),
													    (30, '30'), (31, '31'), (32, '32'), (33, '33'), 
													    (34, '34'), (35, '35'), (36, '36'), (37, '37'), 
													    (38, '38'), (39, '39'), (40, '40'), (41, '41'), 
													    (42, '42'), (43, '43'), (44, '44'), (45, '45'), 
													    (46, '46'), (47, '47'), (48, '48'), (49, '49'), 
													    (50, '50'), (51, '51'), (52, '52'), (53, '53'), 
													    (54, '54'), (55, '55'), (56, '56'), (57, '57'), 
													    (58, '58'), (59, '59')])
														
	endhour = SelectField('endhour', choices=[(1, '1'), (2, '2'), (3, '3'), 
											    (4, '4'), (5, '5'), (6, '6'), (7, '7'), 
											    (8, '8'), (9, '9'), (10, '10'), (11, '11'), (0, '12')])
										  
	endminutes = SelectField('endminutes', choices=[(0, '00'), (1, '01'), (2, '02'), (3, '03'), (4, '04'), 
									  (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), 
									  (10, '10'), (11, '11'), (12, '12'), (13, '13'), 
									  (14, '14'), (15, '15'), (16, '16'), (17, '17'), 
									  (18, '18'), (19, '19'), (20, '20'), (21, '21'), 
									  (22, '22'), (23, '23'), (24, '24'), (25, '25'),
									  (30, '30'), (31, '31'), (32, '32'), (33, '33'), 
									  (34, '34'), (35, '35'), (36, '36'), (37, '37'), 
									  (38, '38'), (39, '39'), (40, '40'), (41, '41'), 
									  (42, '42'), (43, '43'), (44, '44'), (45, '45'), 
									  (46, '46'), (47, '47'), (48, '48'), (49, '49'), 
									  (50, '50'), (51, '51'), (52, '52'), (53, '53'), 
									  (54, '54'), (55, '55'), (56, '56'), (57, '57'), 
									  (58, '58'), (59, '59')])
									  
	ampm1 = SelectField('ampm1', choices=[(1, 'am'), (2, 'pm')])
									  
	ampm2 = SelectField('ampm2', choices=[(1, 'am'), (2, 'pm')])