from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path
from secrets import token_hex

application = Flask(__name__)
application.config['SECRET_KEY'] = str(token_hex(1024))


application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path.join(path.abspath(path=path.dirname(__file__)), 'data.sql')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(app=application)
Migrate(app=application, db=database)


login_manager = LoginManager()
login_manager.init_app(app=application)
login_manager.login_view = 'server.login.login_page_'

from source.controllers.server import server
from source.controllers.functions import functions

application.register_blueprint(blueprint=server)
application.register_blueprint(blueprint=functions)