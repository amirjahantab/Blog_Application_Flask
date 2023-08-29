from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bf0857bbac5c5ed1f25ddd70ccf3a994'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../blog.sqlite'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login first'
login_manager.login_message_category = 'danger'

from blog import routes