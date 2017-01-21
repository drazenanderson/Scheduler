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
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))


	def __repr__(self):

		times = ['9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '1:00', '1:30', '2:00',
			     '2:30', '3:00', '3:30', '4:00', '4:30']

		end = []

		if self.first: 
 			end.append(times[0]) 
 

		if self.second: 
		 	end.append(times[1])
		 

		if self.third: 
		 	end.append(times[2]) 
		 

		if self.fourth: 
		 	end.append(times[3]) 
		 

		if self.fifth: 
		 	end.append(times[4]) 
		 

		if self.sixth: 
		 	end.append(times[5]) 
		 

		if self.seventh: 
		 	end.append(times[6]) 
		 

		if self.eighth: 
		 	end.append(times[7]) 
		 

		if self.ninth: 
		 	end.append(times[8]) 
		 

		if self.tenth: 
		 	end.append(times[9]) 
		 

		if self.eleventh: 
		 	end.append(times[10]) 
		 

		if self.twelfth: 
		 	end.append(times[11]) 
		 

		if self.thirteenth: 
		 	end.append(times[12]) 
		 

		if self.fourteenth: 
		 	end.append(times[13]) 
		 

		if self.fifteenth: 
		 	end.append(times[14]) 
		 

		if self.sixteenth: 
		 	end.append(times[15])

		return "-".join(end) 


	def find_match(self, schedule):

		match = []
		optimal = []
		optimalstring = 'No match'
		teststring = ""
		i = 0

		sched_list = [self.first, self.second, self.third, self.fourth, self.fifth, self.sixth, self.seventh, self.eighth,
					  self.ninth, self.tenth, self.eleventh, self.twelfth, self.thirteenth, self.fourteenth, self.fifteenth,
					  self.sixteenth]

		compare = [schedule.first, schedule.second, schedule.third, schedule.fourth, schedule.fifth, schedule.sixth, 
				   schedule.seventh, schedule.eighth, schedule.ninth, schedule.tenth, schedule.eleventh, schedule.twelfth, 
				   schedule.thirteenth, schedule.fourteenth, schedule.fifteenth, schedule.sixteenth]

		times = ['9:00 am', '9:30 am', '10:00 am', '10:30 am', '11:00 am', '11:30 am', '12:00 pm', '12:30 pm', '1:00 pm',
				 '1:30 pm', '2:00 pm', '2:30 pm', '3:00 pm', '3:30 pm', '4:00 pm', '4:30 pm']

		for a, b in zip(sched_list, compare):
			if a and b:
				match.append(times[i])
			else:
				match = []

			if len(match) > len(optimal):
				optimal.append(match)

			i += 1

		#if len(optimal) > 0:
		#	optimalstring = '' + optimal[0] + ' - ' + optimal[-1]

		return optimal

	def get_date(self):

		date = self.date


		months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
		 	 	  'September', 'October', 'November', 'December']

		month = months[date.month - 1]
		year = date.year
		day = date.day

		return str(month) + " " + str(day) + ", " + str(year)

	def list_notation(self):

		final = []


		sched_list = [self.first, self.second, self.third, self.fourth, self.fifth, self.sixth, self.seventh, self.eighth,
					  self.ninth, self.tenth, self.eleventh, self.twelfth, self.thirteenth, self.fourteenth, self.fifteenth,
					  self.sixteenth]

		for a in sched_list:

			if a:

				final.append('x')
			else:

				final.append(' ')

		return final







class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	appointment = db.relationship('Appointment', backref='customer', lazy='dynamic')
	windows = db.relationship('Window', backref='customer', lazy='dynamic')
	parent = db.relationship('User', back_populates='customer')

	def __repr__(self):
		return '<Customer %r>' % (self.parent.username)


class Client(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	appointment = db.relationship('Appointment', backref='client', lazy='dynamic')
	windows = db.relationship('Window', backref='client', lazy='dynamic')
	parent = db.relationship('User', back_populates='client')

	def __repr__(self):
		return '<Client %r>' % (self.parent.username)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64))
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(64))
	customer = db.relationship('Customer', back_populates='parent')
	client = db.relationship('Client', back_populates='parent')
	first = db.Column(db.String(64))
	last = db.Column(db.String(64))



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

	def is_not_client(self):
		return self.client is None


class Appointment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
	schedule_id = db.Column(db.Integer, db.ForeignKey('window.id'))
	address = db.Column(db.String(120))
	confirmed = db.Column(db.Boolean)
	

class Frame(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date)
	start = db.Column(db.Integer)
	end = db.Column(db.Integer)


