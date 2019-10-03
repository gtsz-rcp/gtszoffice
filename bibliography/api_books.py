from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import abort
from lib.db import db
from lib.app import api
import lib.auth as Auth
from .models_books import Books as BooksModel
from .models_books import Colorspace


class BookDataObject:

    def params(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('slug', type=str)
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('subtitle', type=str)
        parser.add_argument('language', type=str)
        parser.add_argument('place', type=str, default='Seoul')
        parser.add_argument('medium', type=str)
        parser.add_argument('page_amt', type=int)
        parser.add_argument('binding', type=str)
        parser.add_argument(
            'colorspace',
            type=str,
            required=True,
            default='CMYK')
        parser.add_argument('summary', type=str)
        parser.add_argument('toc', type=str)
        parser.add_argument('publishedtime', type=str, required=True)

    def to_json(self, Book: BooksModel):
        data = {
            'id': Book.id,
            'slug': Book.slug,
            'title': Book.title,
            'subtitle': Book.subtitle,
            'language': Book.language,
            'place': Book.place,
            'medium': Book.medium,
            'page_amt': Book.page_amt,
            'binding': Book.binding,
            'colorspace': Book.colorspace.value,
        }

        data['colorspace_label'] = Book.colorspace.label()
        return data

    def __get_book_or_abort(self, book_id):
        Book = BooksModel.query.get(book_id)
        if Book is None:
            message = f'Book(id: {book_id} not exist)'
            abort(404, message=message)
        return Book

    def __abort_colorspace_is_not_available(self, colorspace_value):
        if getattr(Colorspace, colorspace_value) is None:
            message = f"colorspace value: {colorspace_value} is not available"
            abort(422, message=message)

    def create(self):
        Auth.abort_if_not_admin()

        params = self.params().parse_args()
        Book = BooksModel()
        Book.slug = params['slug']
        Book.title = params['title']
        Book.subtitle = params['subtitle']
        Book.language = params['language']
        Book.place = params['place']
        Book.medium = params['medium']
        Book.page_amt = params['page_amt']
        Book.binding = params['binding']
        Book.colorspace = params['colorspace']

        self.__abort_colorspace_is_not_available(params['colorspace'])

        db.session.add(Book)
        db.session.commit()
        return self.to_json(Book)

    def update(self, book_id):
        Auth.abort_if_not_admin()

        Book = self.__get_book_or_abort(book_id)

        params = self.params().parse_args()
        Book.slug = params['slug']
        Book.title = params['title']
        Book.subtitle = params['subtitle']
        Book.language = params['language']
        Book.place = params['place']
        Book.medium = params['medium']
        Book.page_amt = params['page_amt']
        Book.binding = params['binding']
        Book.colorspace = params['colorspace']

        self.__abort_colorspace_is_not_available(params['colorspace'])

        db.session.commit()

        return self.to_json(BooksModel.query.get(book_id))

    def delete(self, book_id):
        Auth.abort_if_not_admin()

        Book = self.__get_book_or_abort(book_id)

        db.session.delete(Book)
        db.session.commit()
        return {'message': f'Book(id: {book_id} deleted)'}

    def get(self, **kwargs):
        value = ''
        if 'book_id' in kwargs:
            value = kwargs['book_id']
            Book = BooksModel.query.get(kwargs['book_id'])
        elif 'book_slug' in kwargs:
            value = kwargs['book_slug']
            Book = BooksModel.query.filter_by(slug=kwargs['book_slug']).first()

        if Book is None:
            abort(404, f'Book({value}) is not exist')
        return self.to_json(Book)

    def lists(self):
        Books = []
        query = BooksModel.query.all()
        if query is not None:
            for book in query:
                Books.append(self.to_json(book))

        return Books


@api.resource('/bibliography/books/')
class Books(Resource):
    def get(self):
        bdo = BookDataObject()
        return bdo.lists()

    def post(self):
        bdo = BookDataObject()
        return bdo.create()


@api.resource('/bibliography/books/<string:slug>')
class BooksWithSlug(Resource):
    def get(self, slug):
        bdo = BookDataObject()
        return bdo.get(book_slug=slug)


@api.resource('/bibliography/books/<int:book_id>')
class BooksWithId(Resource):
    def get(self, book_id):
        bdo = BookDataObject()
        return bdo.get(book_id=book_id)

    def put(self, book_id):
        bdo = BookDataObject()
        return bdo.update(book_id)

    def delete(self, book_id):
        bdo = BookDataObject()
        return bdo.delete(book_id)
