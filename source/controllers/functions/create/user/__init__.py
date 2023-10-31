from flask import Blueprint
from source.controllers.functions.create.user.function import register_page

create_user = Blueprint(name='create_user', import_name=__name__)

@create_user.route('/register', methods=['POST', 'GET'])
def _register_page_():
    return register_page()