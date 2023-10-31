from flask import Blueprint
from source.controllers.server.home.function import main_root, home_page


home = Blueprint(name='home', import_name=__name__)

@home.route('/')
def _main_root_page_():
    return main_root()


@home.route('/home')
def _home_page_():
    return home_page()
