from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import basedir

app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

db = SQLAlchemy(app)

from app import views, models