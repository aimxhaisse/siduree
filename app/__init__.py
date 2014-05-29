from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# main app (flask)
app = Flask(__name__)
app.secret_key = 'mekelcafay?siduri!'
app.config.from_object('config')

# db (flask-sqlalchemy)
db = SQLAlchemy(app)

# login manager (flask-login)
login_manager = LoginManager()
login_manager.init_app(app)

from app import views, models, misc
