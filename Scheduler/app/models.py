from app import db



class Window(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date)
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
	customer = db.relationship('Customer', backref='window', lazy='dynamic')
	client = db.relationship('Client', backref='window', lazy='dynamic')
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		times = ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '1:00', '1:30', '2:00',
			     '2:30', '3:00', '3:30', '4:00', '4:30']

		sched_list = [self.first, self.second, self.third, self.fourth, self.fifth, self.sixth, self.seventh, self.eighth,
					  self.ninth, self.tenth, self.eleventh, self.twelfth, self.thirteenth, self.fourteenth, self.fifteenth,
					  self.sixteenth]

		end = []

		i = 0

		for time in times:
			if sched_list[i]:
				end.append[time]

		return '-'.join(end)



	def find_match(self, window):
		sched_list = [self.first, self.second, self.third, self.fourth, self.fifth, self.sixth, self.seventh, self.eighth,
					  self.ninth, self.tenth, self.eleventh, self.twelfth, self.thirteenth, self.fourteenth, self.fifteenth,
					  self.sixteenth]

		compare = [window.first, window.second, window.third, window.fourth, window.fifth, window.sixth, window.seventh, window.eighth,
				   window.ninth, window.tenth, window.eleventh, window.twelfth, window.thirteenth, window.fourteenth, window.fifteenth,
				   window.sixteenth]

		times = ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '1:00', '1:30', '2:00',
			     '2:30', '3:00', '3:30', '4:00', '4:30']

		match = []
		optimal = []
		i = 0

		for block in sched_list:
			if block == compare[i] and block:
				match.append(times[i])
			else:
				match = []

			if match.len() > optimal.len():
				optimal = match

		return optimal






class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	appointment = db.relationship('Appointment', backref='customer', lazy='dynamic')
	window_id = db.Column(db.Integer, db.ForeignKey('window.id'))


class Client(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	appointment = db.relationship('Appointment', backref='client', lazy='dynamic')
	window_id = db.Column(db.Integer, db.ForeignKey('window.id'))



class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(64))
	customer = db.relationship('Customer', backref='user', lazy='dynamic')
	client = db.relationship('Client', backref='user', lazy='dynamic')
	first = db.Column(db.String(64))
	last = db.Column(db.String(64))
	windows = db.relationship('Window', backref='user', lazy='dynamic')



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

	def is_client(self):
		return self.client is None


class Appointment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
	schedule_id = db.Column(db.Integer, db.ForeignKey('window.id'))
	address = db.Column(db.String(120))


