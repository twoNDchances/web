from flask import Blueprint, redirect, url_for
from flask_login import login_required
from source.controllers.server.logout.function import logout_page

logout = Blueprint(name='logout', import_name=__name__)

@logout.route('/logout')
@login_required
def logout_page_():
    return logout_page()
