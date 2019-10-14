from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import abort
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHash
from lib.db import db
from lib.app import api
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
            'password': User.password,
            'createtime': User.createtime
        }

        if Auth.is_login() is False:
            del data['password']
        elif Auth.is_admin() is False and data['email'] != Auth.get_login('email'):
            del data['password']

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

    def get(self, user_id):
        User = UsersModel.query.get(user_id)
        if User is None:
            message = self._messages['user_id_not_exists'].\
                format(user_id=user_id)
            abort(404, message=message)
        return self.to_json(User)

    def lists(self):
        Auth.abort_if_not_login()
        Users = []
        query = UsersModel.query.all()
        if query is not None:
            for user in query:
                Users.append(self.to_json(user))
        return Users

    def udpate(self, user_id):
        User = UsersModel.query.get(user_id)
        if User is None:
            message = self._messages['user_id_not_exists'].\
                format(user_id=user_id)
            abort(404, message=message)

        params = self.params().parse_args()
        User.type = getattr(UsersType, params['type'])
        User.name = params['name']
        User.password = ph.hash(params['password'])

        db.session.commit()
        return self.to_json(UsersModel.query.get(user_id))

    def delete(self, user_id):
        Auth.abort_if_not_login()

        User = UsersModel.query.get(user_id)
        if User is None:
            message = self.messages['user_id_not_exists'].\
                format(user_id=user_id)
            abort(404, message=message)

        if User.email != Auth.get_login('email') and Auth.is_admin() is False:
            abort(403, 'not allowed')
        db.session.delete(User)
        db.session.commit()

        return {'message': 'User({email}) deleted'.format(email=User.email)}

    def is_login(self):
        Auth.abort_if_not_login()
        return {'message': 1}

    def is_admin(self):
        Auth.abort_if_not_admin()
        return {'message': 1}

    def login(self):
        params = self.login_params().parse_args()
        User = UsersModel.query.filter_by(email=params['email']).first()
        error_message = "Login failed(email or password is not matched)"

        if User is None:
            abort(401, message=error_message)

        try:
            if ph.verify(User.password, params['password']) is False:
                abort(401, message=error_message)
        except InvalidHash:
            abort(401, message='Invalid hash')


        if ph.check_needs_rehash(User.password):
            self.__rehash(User, params['password'])

        Auth.login_proc(**self.to_json(User))
        return {'message': 'success'}

    def __rehash(self, User: UsersModel, password: str):
        User.password = ph.hash(password)
        db.session.commit()

    def logout(self):
        if Auth.is_login() is False:
            abort(401, message="Login first")

        return Auth.logout_proc()


@api.resource('/users/')
class Users(Resource):
    def get(self):
        udo = UserDataObject()
        return udo.lists()

    def post(self):
        udo = UserDataObject()
        return udo.create()


@api.resource('/users/<int:user_id>')
class UsersWithId(Resource):
    def get(self, user_id):
        udo = UserDataObject()
        return udo.get(user_id)


@api.resource('/auth/login')
class UserLogin(Resource):
    def post(self):
        udo = UserDataObject()
        return udo.login()

    def get(self):
        udo = UserDataObject()
        return udo.is_login()


@api.resource('/auth/logout')
class UserLogout(Resource):
    def get(self):
        udo = UserDataObject()
        return udo.logout()
