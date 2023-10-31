from flask import Blueprint
from source.controllers.server.login.function import login_page
login = Blueprint(name='login', import_name=__name__)

@login.route('/login', methods=['POST', 'GET'])
def login_page_():
    return login_page()
