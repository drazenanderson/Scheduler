from app import db



class Window(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime)
	first = db.Column(db.Boolean)
	second = db.Column(db.Boolean)
	third = db.Column(db.Boolean)
	fourth = db.Column(db.Boolean)
	fifth = db.Column(db.Boolean)
	sixth = db.Column(db.Boolean)
	seventh = db.Column(db.Boolean)
	eighth = db.Column(db.Boolean)
	ninth = db.Column(db.Boolean)
	tenth = db.Column(db.Boolean)
	eleventh = db.Column(db.Boolean)
	twelfth = db.Column(db.Boolean)
	thirteenth = db.Column(db.Boolean)
	fourteenth = db.Column(db.Boolean)
	fifteenth = db.Column(db.Boolean)
	sixteenth = db.Column(db.Boolean)
	appointment = db.relationship('Appointment', backref='window', lazy='dynamic')


class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	appointment = db.relationship('Appointment', backref='customer', lazy='dynamic')


class Client(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	appointment = db.relationship('Appointment', backref='client', lazy='dynamic')



class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(120), index=True, unique=True)
	phone = db.Column(db.String())
	password = db.Column(db.String(64), index=True, unique=True)
	customer = db.relationship('Customer', backref='user', lazy='dynamic')
	client = db.relationship('Client', backref='user', lazy='dynamic')



	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id) # python 2
		except NameError:
			return str(self.id) # python 3

	def __repr__(self):
		return '<User %r>' % (self.username)


class Appointment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
	schedule_id = db.Column(db.Integer, db.ForeignKey('window.id'))
	address = db.Column(db.String(120))


