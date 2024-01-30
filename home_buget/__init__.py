"""This are built-in modules, which are part of python standard library"""
import os
import secrets


"""This are third party modules or package that need to 
be install seperately using pip """
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
from flask_login import login_manager, LoginManager


"""Flask Instanciation"""
app = Flask(__name__)


"""Database configuration"""
secrets_token = secrets.token_urlsafe(10)
app_database = os.path.join(os.path.dirname(__file__), "database")
database_path = os.path.join(app_database, "BUDGET.db")


"""App Configuration"""
app.config["SECRET_KEY"] = secrets_token
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
app.config["ASSETS_DEBUG"] = False


"""Packages Instanciation"""
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)
migrate = Migrate(app, db)


"""Login Instanciation"""
login_manager = LoginManager(app)
login_manager.login_view = "view.home"
login_manager.login_message_category = "info"

assets = Environment(app)




assets.register()
assets.register()
assets.register()


from home_buget.auth.routes import authent
from home_buget.view.routes import homepage
from home_buget.dashboard.routes import controller


app.register_blueprint(authent, url_prefix="/")
app.register_blueprint(homepage, url_prefix="/")
app.register_blueprint(controller, url_prefix="/")