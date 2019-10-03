from falsk_restful import Resource
from flask_restful import reqparse
from flask_restful import abort
from lib.db import db
from lib.app import api
import lib.auth as Auth
from artsts.models import Artists as ArtistsModel
from models_books import Books as BooksModel
from models_bookpartners import BookPartners as BookPartnersModel
from models_bookpartners import BookPartnerType


class BookPartnerDataObject:

    def params(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('order', type=int)
        parser.add_argument('type', type=str, default='artist')
        parser.add_argument('artist', type=int, required=True)
        parser.add_argument('book', type=int, required=True)

        return parser

    def __abort_type_not_available(self, type_value):
        if getattr(BookPartnerType, type_value) is None:
            message = f'Book partner value: {type_value} is not available'
            abort(422, message=message)

    def __get_artist_or_abort(self, artist_id):
        Artist = ArtistsModel.query.get(artist_id)
        if Artist is None:
            message = f'Artist({artist_id}) is not exist'
            abort(422, message=message)
        return Artist

    def __get_book_or_abort(self, book_id):
        Book = BooksModel.query.get(book_id)
        if Book is None:
            message = f'Book(id: {book_id}) is not exist'
            abort(422, message=message)
        return Book

    def __get_partner_or_abort(self, partner_id):
        Partner = BookPartnersModel.query.get(partner_id)
        if Partner is None:
            message = f'Partner(id: {partner_id}) is not exist'
            abort(404, message=message)
        return Partner

    def to_json(self, Partner: BookPartnersModel):
        data = {
            'id': Partner.id,
            'order': Partner.order,
            'type': Partner.type,
            'artist': Partner.artist,
            'book': Partner.book
        }

        data['artist_data'] = self.__get_artist_or_abort(Partner.artist)
        data['book_data'] = self.__get_book_or_abort(Partner.book)

        return data

    def create(self):
        Auth.abort_if_not_admin()

        params = self.params().parse_args()
        Partner = BookPartnersModel()
        Partner.order = params['order']
        Partner.type = params['type']
        Partner.artist = params['artist']
        self.__get_artist_or_abort(params['artist'])

        Partner.book = params['book']
        self.__get_book_or_abort(params['book'])

        db.session.add(Partner)
        db.session.commit()
        return self.to_json(Partner)

    def update(self, partner_id):
        Auth.abort_if_not_admin()

        Partner = self.__get_partner_or_abort(partner_id)

        params = self.params().parse_args()
        Partner.order = params['order']
        Partner.type = params['type']
        self.__abort_type_not_available(params['type'])

        Partner.artist = params['artist']
        self.__get_artist_or_abort(params['artist'])

        Partner.book = params['book']
        self.__get_book_or_abort(params['book'])

        db.session.commit()

        return self.to_json(BookPartnersModel.query.get(partner_id))

    def delete(self, partner_id):
        Auth.abort_if_not_admin()

        Partner = self.__get_partner_or_abort(partner_id)

        db.session.delete(Partner)
        db.session.commit()
        return {'message': f'Partner(id: {partner_id}) deleted'}

    def get(self, partner_id):
        Partner = self.__get_partner_or_abort(partner_id)
        return self.to_json(Partner)

    def lists(self):
        Partners = []
        query = BookPartnersModel.query.all()
        if query is not None:
            for partner in query:
                Partners.append(self.to_json(partner))

        return Partners


@api.resource('/bibliography/partners/')
class BookPartners(Resource):
    def get(self):
        pdo = BookPartnerDataObject()
        return pdo.lists()

    def post(self):
        pdo = BookPartnerDataObject()
        return pdo.create()


@api.resource('/bibliography/partners/<int:partner_id>')
class BookPartnersWithId(Resource):
    def get(self, partner_id):
        pdo = BookPartnerDataObject()
        return pdo.get(partner_id)

    def put(self, partner_id):
        pdo = BookPartnerDataObject()
        return pdo.udpate(partner_id)

    def delete(self, partner_id):
        pdo = BookPartnerDataObject()
        return pdo.delete(partner_id)