from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import abort
from lib.db import db
from lib.app import api
import lib.auth as Auth
from .models import Artists as ArtistsModel
from users.models import Users as UsersModel


class ArtistsDataObject:

    def __init__(self):
        self.error = None
        self.error_no = 403

    def to_json(self, Artist: ArtistsModel):
        data = {
            'id': Artist.id,
            'name': Artist.name,
            'name_en': Artist.name_en,
            'user': Artist.user
        }

        if data['user'] is not None:
            data['user_data'] = UsersModel.query.get(data['user'])

        return data
    
    def create(self, data):
        Artist = ArtistsModel()
        Artist.name = data['name']
        Artist.name_en = data['name_en']

        if data['user'] is not None:
            User = UsersModel.query.get(params['user'])

            if User is None:
                self.error = 'user(id: {user}) not exists'.\
                    format(user=data['user'])
                return False

        db.session.add(Artist)
        db.session.commit()
        return self.to_json(Artist)
    
    def get(self, artist_id):
        Artist = ArtistsModel.query.get(artist_id)
        if Artist is None:
            self.error = f'Artist(id: {artist_id}) not exits'
            self.error_no = 404
            return False

        return self.to_json(Artist)


class ArtistsDataTransferObject:

    def params(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('name_en', type=str)
        parser.add_argument('user', type=int)

        return parser

    def to_json(self, Artist: ArtistsModel):
        data = {
            'id': Artist.id,
            'name': Artist.name,
            'name_en': Artist.name_en,
            'user': Artist.user
        }

        if data['user'] is not None:
            data['user_data'] = UsersModel.query.get(data['user'])

        return data

    def create(self):
        Auth.abort_if_not_login()
        adt = ArtistsDataObject()
        params = self.params().parse_args()
        rtn = adt.create(params)
        if rtn is False:
            abort(adt.error_no, message=adt.error)
        return rtn

    def update(self, artist_id):
        Auth.abort_if_not_login()

        Artist = ArtistsModel.query.get(artist_id)
        if Artist is None:
            message = f'Artist(id: {artist_id} not exist)'
            abort(404, message=message)

        params = self.params().parse_args()
        Artist.name = params['name']
        Artist.name_en = params['name_en']

        db.session.commit()
        return self.to_json(ArtistsModel.query.get(artist_id))

    def delete(self, artist_id):
        Auth.abort_if_not_login()

        Artist = ArtistsModel.query.get(artist_id)
        if Artist is None:
            message = f'Artist(id: {artist_id}) not exists'
            abort(404, message=message)

        if Artist.user is not None:
            if Auth.is_admin() is False and Auth.get_login('id') != Artist.user:
                message = f'permission denied'
                abort(403, message)

        db.session.delete(Artist)
        db.session.commit()

        return {'message': f'Artist(id: {artist_id}) deleted'}

    def get(self, artist_id):
        adt = ArtistsDataObject()
        Artist = adt.get(artist_id)
        if Artist is False:
            abort(adt.error_no, message=adt.error)

        return Artist

    def lists(self):
        Artists = []
        query = ArtistsModel.query.all()
        if query is not None:
            for artist in query:
                Artists.append(self.to_json(artist))

        return Artists


@api.resource('/artists/')
class Artists(Resource):
    def get(self):
        ado = ArtistsDataTransferObject()
        return ado.lists()

    def post(self):
        ado = ArtistsDataTransferObject()
        return ado.create()


@api.resource('/artists/<int:artist_id>')
class ArtistsWithId(Resource):
    def get(self, artist_id):
        ado = ArtistsDataTransferObject()
        return ado.get(artist_id)

    def put(self, artist_id):
        ado = ArtistsDataTransferObject()
        return ado.update(artist_id)

    def delete(self, artist_id):
        ado = ArtistsDataTransferObject()
        return ado.delete()
