from source.datatable import User
from werkzeug.security import check_password_hash

def query_object_user_by_username(username):
    get_user = User.query.filter_by(username=username)
    return get_user.first()


def check_password(username, password):
    get_password = query_object_user_by_username(username=username).password
    return check_password_hash(pwhash=get_password, password=password)