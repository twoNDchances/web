from source import database, login_manager
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id_user):
    return User.query.get(id_user)


class User(database.Model, UserMixin):

    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(16), unique=True, index=True)
    password = database.Column(database.String(512))

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password=password)
