from flask import Blueprint

functions = Blueprint(name='functions', import_name=__name__)

from source.controllers.functions.create.user import create_user

functions.register_blueprint(blueprint=create_user)