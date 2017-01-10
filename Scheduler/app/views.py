from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm, UserForm
from .models import User

@app.route('/')
@app.route('/index')
@login_required
def index():

	return render_template('index.html')

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





@app.route('/register', methods=['GET', 'POST'])
def register():
	form = UserForm()

	if form.validate_on_submit():

		user = User(username = form.username.data, password = form.password.data, email = form.email.data, 
					phone = form.phone.data)

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
	return redirect(url_for('index'))



@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))