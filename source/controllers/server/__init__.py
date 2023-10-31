from flask import Blueprint, render_template, redirect, url_for

server = Blueprint(name='server', import_name=__name__)

from source.controllers.server.home import home
from source.controllers.server.login import login
from source.controllers.server.logout import logout

server.register_blueprint(blueprint=home)
server.register_blueprint(blueprint=login)
server.register_blueprint(blueprint=logout)
