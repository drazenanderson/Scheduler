from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import and_
from datetime import date
from app import app, db, lm
from .forms import LoginForm, UserForm, WindowForm
from .models import User, Window, Customer, Client, Appointment
import collections

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
@app.route('/index/<int:month>/', methods=['GET', 'POST'])
@app.route('/index/<int:month>/<int:year>/', methods=['GET', 'POST'])
@login_required
def index(month = date.today().month - 1, year = date.today().year):

	if g.user is not None and g.user.is_authenticated:

		form = WindowForm()

		user = g.user

		if month > 11 or month < 0:
			month = date.today().month


		months = [
			('January', 31, date(year, 1, 1).weekday()),
			('February', 28, date(year, 2, 1).weekday()),
			('March', 31, date(year, 3, 1).weekday()),
			('April', 30, date(year, 4, 1).weekday()),
			('May', 31, date(year, 5, 1).weekday()),
			('June', 30, date(year, 6, 1).weekday()),
			('July', 31, date(year, 7, 1).weekday()),
			('August', 31, date(year, 8, 1).weekday()),
			('September', 30, date(year, 9, 1).weekday()),
			('October', 31, date(year, 10, 1).weekday()),
			('November', 30, date(year, 11, 1).weekday()),
			('December', 31, date(year, 12, 1).weekday())
		]

		monthinfo = months[month]

		if form.validate_on_submit():

			is_client = form.status.data

			if is_client:
				client = Client(user_id = user.id)
				test = Client.query.filter(Client.user_id == user.id).first()
				window = Window(date=date(year, month + 1, int(form.day.data)), first=form.first.data, second=form.second.data,
							third=form.third.data, fourth=form.fourth.data, fifth=form.fifth.data, sixth=form.sixth.data,
							seventh=form.seventh.data, eighth=form.eighth.data, ninth=form.ninth.data, tenth=form.tenth.data,
							eleventh=form.eleventh.data, twelfth=form.twelfth.data, thirteenth=form.thirteenth.data, 
							fourteenth=form.fourteenth.data, fifteenth=form.fifteenth.data, sixteenth=form.sixteenth.data, 
							client_id = user.id)

			else:
				client = Customer(user_id = user.id)
				test = Customer.query.filter(Customer.user_id == user.id).first()
				window = Window(date=date(year, month + 1, int(form.day.data)), first=form.first.data, second=form.second.data,
							third=form.third.data, fourth=form.fourth.data, fifth=form.fifth.data, sixth=form.sixth.data,
							seventh=form.seventh.data, eighth=form.eighth.data, ninth=form.ninth.data, tenth=form.tenth.data,
							eleventh=form.eleventh.data, twelfth=form.twelfth.data, thirteenth=form.thirteenth.data, 
							fourteenth=form.fourteenth.data, fifteenth=form.fifteenth.data, sixteenth=form.sixteenth.data,
							customer_id = user.id)

			
			if test is None:
				flash('New client made')
				if is_client:
					flash('client')
					user.client.append(client)
				else:
					flash('user')
					user.customer.append(client)


			else:
				if duplicate(test.windows, date(year, month + 1, int(form.day.data))):
					flash('DELETED')
					if is_client:
						Window.query.filter(Window.client_id == user.id, Window.date == date(year, month + 1, int(form.day.data))).delete()
					else:
						Window.query.filter(Window.customer_id == user.id, Window.date == date(year, month + 1, int(form.day.data))).delete()

				
				test.windows.append(window)


			
			db.session.commit()


			flash('Updated successfully.')

			fits = find_match(window, is_client)
			session['matches'] = fits
			session['month'] = monthinfo[0]
			session['year'] = year
			session['day'] = int(form.day.data)



			if len(fits) > 0 and fits:
				return redirect(url_for('confirmation'))
			else:
				flash('No match found.')
				return redirect(url_for('index'))


		return render_template('index.html',
								user=user,
								month = month,
								monthinfo = monthinfo,
							    year = year,
								form = form)


	if g.user is None:
		return redirect(url_for('login'))



@app.route('/appointments')
@app.route('/appointments/<int:month>')
@app.route('/appointments/<int:month>/<int:year>')
@app.route('/appointments/<int:month>/<int:year>/<int:day>')
@login_required
def appointments(month = date.today().month - 1, year = date.today().year, day = 0):
	user = g.user

	months = [
		('January', 31, date(year, 1, 1).weekday()),
		('February', 28, date(year, 2, 1).weekday()),
		('March', 31, date(year, 3, 1).weekday()),
		('April', 30, date(year, 4, 1).weekday()),
		('May', 31, date(year, 5, 1).weekday()),
		('June', 30, date(year, 6, 1).weekday()),
		('July', 31, date(year, 7, 1).weekday()),
		('August', 31, date(year, 8, 1).weekday()),
		('September', 30, date(year, 9, 1).weekday()),
		('October', 31, date(year, 10, 1).weekday()),
		('November', 30, date(year, 11, 1).weekday()),
		('December', 31, date(year, 12, 1).weekday())
	]

	monthinfo = months[month]

	if day > 0:
		if user.is_not_client():
			times = Customer.query.join(Customer.windows).filter(Customer.user_id == user.id, Window.date == date(year, month + 1, day)).first()
			others = Client.query.join(Client.windows).filter(Window.date == date(year, month + 1, day)).all()
		else:

			times = Client.query.join(Client.windows).filter(Client.user_id == user.id, Window.date == date(year, month + 1, day)).first()
			others = Customer.query.join(Customer.windows).filter(Window.date == date(year, month + 1, day)).all()

		
		if times:	

			for window in times.windows:
				if window.date == date(year, month + 1, day):
					correctWindow = window


			return render_template('appointments.html',
								   user=user,
								   window=correctWindow,
								   others=others,
								   month=month,
								   year=year,
								   day=day,
								   monthinfo=monthinfo,
								   appointments=True)

	

	times = Customer.query.first()
	others = Client.query.all()
	correctWindow = times.windows[0]


	flash('No appointments found for ' + user.username)
	return render_template('appointments.html',
							user=user,
							window=correctWindow,
							others=others,
							month=month,
							year=year,
							day=day,
							monthinfo=monthinfo,
							appointments=False)




@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		
		username = form.username.data
		password = form.password.data
		remember = form.remember_me.data

		q = User.query.filter(User.username == username, User.password == password).first()

		if q:

			login_user(q)

			flash('Logged in successfully.')

			next = request.args.get('next')


			#if not is_safe_url(next):
			#	return abort(400)

			return redirect(next or url_for('index'))

		else:

			flash('Incorrect login.')
			return render_template('login.html', form=form, title='Home')

	return render_template('login.html', form=form, title='Home')



@app.route('/confirmation', methods=['GET', 'POST'])
@login_required
def confirmation():
	user = g.user
	matches = session['matches']
	month = session['month']
	year = session['year']
	day = session['day']

	return render_template('confirmation.html',
						    matches=matches,
						    user=user,
						    month=month,
						    day=day,
						    year=year)



@app.route('/register', methods=['GET', 'POST'])
def register():
	form = UserForm()

	if form.validate_on_submit():

		flash('Registering...')

		user = User(username = form.username.data, password = form.password.data, email = form.email.data, 
					first = form.first.data, last = form.last.data)


		db.session.add(user)
		db.session.commit()

		login_user(user)

		return redirect(url_for('index'))


	flash('Invalid entry.')

	return render_template('register.html',
							form = form,
							title = 'Home')






@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))



@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



def find_match(timeframe, is_client):
	matches = {}

	if is_client:

		windows = Customer.query.join(Customer.windows).filter(Window.date == timeframe.date).all()

	else:

		windows = Client.query.join(Client.windows).filter(Window.date == timeframe.date).all()


	for schedule in windows:
		matches[str(schedule.parent.username)] = []

		for block in schedule.windows:
			i = 0

			if block and block.date == timeframe.date:
				hits = timeframe.find_match(block)
			else:
				hits = "No match"

			for hit in hits:

				if hit not in matches[str(schedule.parent.username)]:
				
					matches[str(schedule.parent.username)].append(hit)

	od = collections.OrderedDict(sorted(matches.items()))

	return od


@app.before_request
def before_request():
    g.user = current_user


def duplicate(windows, date):

	user = g.user

	for window in windows:
		if window.date == date:
			return True

	return False

