from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from datetime import date
from app import app, db, lm
from .forms import LoginForm, UserForm, WindowForm
from .models import User, Window, Customer, Client, Appointment

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
@app.route('/index/<username>', methods=['GET', 'POST'])
@app.route('/index/<username>/<int:month>', methods=['GET', 'POST'])
@app.route('/index/<username>/<int:month>/<int:year>', methods=['GET', 'POST'])
@login_required
def index(username = None, month = date.today().month - 1, year = date.today().year):

	form = WindowForm()

	user = User.query.filter_by(username=username).first()

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

		is_client = True

		window = Window(date=date(year, month, form.day.data), first=form.first.data, second=form.second.data,
						third=form.third.data, fourth=form.fourth.data, fifth=form.fifth.data, sixth=form.sixth.data,
						seventh=form.seventh.data, eighth=form.eighth.data, ninth=form.ninth.data, tenth=form.tenth.data,
						eleventh=form.eleventh.data, twelfth=form.twelfth.data, thirteenth=form.thirteenth.data, 
						fourteenth=form.fourteenth.data, fifteenth=form.fifteenth.data, sixteenth=form.sixteenth.data, user=user)
		db.session.add(window)
		db.session.commit()

		customer = Customer.query.filter_by(user_id = user.id).first()
		client = Client.query.filter_by(user_id = user.id).first()
		if customer is not None:
			customer.window = window
			is_client = False
			db.session.add(customer)
			db.session.commit()
		elif client is not None:
			client.window = window
			db.session.add(client)
			db.session.commit()


		flash('Updated successfully.')

		fits = find_match(window, is_client)
		if fits.len() > 0:
			flash('Matches found.')
			return redirect(url_for('confirmation', username=username, matches=fits))
		else:
			return redirect(url_for('index', username=username))

	else:
		flash('Did not submit.')

	if username is None:
		return redirect(url_for('login'))

	return render_template('index.html',
						   user=user,
						   month = month,
						   monthinfo = monthinfo,
						   year = year,
						   form = form)


@app.route('/appointments')
@app.route('/appointments/<username>')
@login_required
def appointments(username):
	user = User.query.filter_by(username=username).first()

	if user.is_client():
		others = Customer.query.all()
	else:
		others = Client.query.all()

	return render_template('appointments.html',
						   user=user,
						   others=others)




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

			return redirect(next or url_for('index', username=q.username))

		else:

			flash('Incorrect login.')
			return render_template('login.html', form=form, title='Home')

	return render_template('login.html', form=form, title='Home')



@app.route('/confirmation', methods=['GET', 'POST'])
@login_required
def confirmation(username, matches):
	user = User.query.filter_by(username=username).first()

	return render_template('confirmation.html',
						   matches=matches,
						   user=user)



@app.route('/register', methods=['GET', 'POST'])
def register():
	form = UserForm()

	if form.validate_on_submit():

		flash('Registering...')

		user = User(username = form.username.data, password = form.password.data, email = form.email.data, 
					first = form.first.data, last = form.last.data)

		if form.status.data == 'client':
			client = Client(user=user)
			db.session.add(client)
		elif form.status.data == 'customer':
			customer = Customer(user=user)
			db.session.add(customer)

		db.session.add(user)
		db.session.commit()

		login_user(user)

		return redirect(url_for('index', username=user.username))


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

		windows = Customer.query.filter(window.date == timeframe.date).all()

	else:

		windows = Client.query.filter(window.date == timeframe.date).all()

	for window in windows:

		hit = timeframe.find_match(window.window)
		matches[window.user.username] = hit

	return matches


