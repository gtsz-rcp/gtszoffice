from flask import session
from flask_restful import abort


def login_proc(**kwargs):
    session['user_id'] = kwargs['id']
    session['user_type'] = kwargs['type_str']
    session['user_email'] = kwargs['email']
    session['user_name'] = kwargs['name']


def logout_proc(**kwargs):
    user_keys = ('user_id', 'user_type', 'user_email', 'user_name')
    for key in user_keys:
        session.pop(key, None)
    return True


def is_login():
    if 'user_id' in session:
        return True
    return False


def is_admin():
    if is_login() is False:
        return False
    if 'user_type' not in session:
        return False
    if session['user_type'] == 'admin':
        return True
    return False


def abort_if_not_login():
    if is_login() is False:
        return abort(401, message="Login required")
    return True


def abort_if_not_admin():
    if abort_if_not_login() is not True:
        return False
    if is_admin() is not True:
        return abort(401, message="Adminstrator only")
    return True
