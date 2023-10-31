from flask import redirect, url_for
from flask_login import logout_user


def logout_page():
    logout_user()
    return redirect(url_for('server.home.main_root_page_'))