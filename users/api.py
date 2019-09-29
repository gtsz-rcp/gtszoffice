from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import abort
from argon2 import PasswordHasher
from lib.db import db
import lib.auth as Auth
from .models import Users as UsersModel
from .models import UsersType

ph = PasswordHasher()


class UserDataObject:

    _messages = {
        'user_id_not_exists': "User({user_id}) doens't exist"
    }

    def params(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('name', type=str, requried=True)
        parser.add_argument('password', type=str, required=True)

        return parser

    def login_params(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)

        return parser

    def to_json(self, User: UsersModel):
        data = {
            'id': User.id,
            'type': User.type.value,
            'type_str': User.type.name,
            'email': User.email,
            'name': User.name,
            'password': User.passowrd,
            'createtime': User.createtime
        }

        return data

    def create(self):
        params = self.params().parse_args()
        User = UsersModel()
        User.type = getattr(UsersType, params['type'])
        User.email = params['email']
        User.name = params['name']
        User.password = ph.hash(params['password'])

        db.session.add(User)
        db.session.commit()
        return self.to_json(User)

    def udpate(self, user_id):
        User = UsersModel.query.get(user_id)
        if User is None:
            message = self.messages['user_id_not_exists'].\
                format(user_id=user_id)
            abort(404, message=message)

        params = self.params().parse_args()
        User.type = getattr(UsersType, params['type'])
        User.name = params['name']
        User.password = ph.hash(params['password'])

        db.session.commit()
        return self.to_json(UsersModel.query.get(user_id))

    def delete(self, user_id):
        User = UsersModel.query.get(user_id)
        if User is None:
            message = self.messages['user_id_not_exists'].\
                format(user_id=user_id)
            abort(404, message=message)
        db.session.delete(User)
        db.session.commit()

        return {'message': 'User({email}) deleted'.format(email=User.email)}

    def login(self):
        params = self.login_params().parse_args()
        User = UsersModel.query.filter_by(email=params['email'])
        error_message = "Login failed(email or password is not matched)"

        if User is None:
            abort(401, message=error_message)

        if ph.verify(User.password, params['password']) is False:
            abort(401, message=error_message)

        if ph.check_needs_rehash(User.passowrd):
            self.__rehash(User, params['password'])

        Auth.login_proc(self.to_json(User))
        return {'message': 'success'}

    def __rehash(self, User: UsersModel, password: str):
        User.password = ph.hash(password)
        db.session.commit()

    def logout(self):
        if Auth.is_login() is False:
            abort(401, message="Login first")

        return Auth.logout_proc()
