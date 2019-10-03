from datetime import datetime
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import abort
from lib.db import db
from lib.db import datetime_zero
from lib.app import api
from .models import Pages as PagesModel
from .models import PagesType
from .models import init_from_dict


class PagesDataObject:

    def delete_by_id(self, pageType, page_id):
        Page = PagesModel.query.get(page_id)
        if Page is None or Page.type != getattr(PagesType, pageType):
            abort(404, message="{type}(id: {page_id}) doesn't exist".format(type=pageType, page_id=page_id))

        Page.deletetime = datetime_zero()
        db.session.commit()
        return {'message': '{type}(id: {page_id}) deleted'.format(type=pageType, page_id=page_id)}

    def get_by_id(self, pageType, page_id):
        Page = PagesModel.query.get(page_id)
        if Page is None or Page.type != PagesType.page:
            abort(404, message="{type}(id: {page_id}) doesn't exist".format(type=pageType, page_id=page_id))
        return self.to_json(Page)

    def get_by_slug(self, pageType, slug):
        Page = PagesModel.query.\
            filter(PagesModel.slug == slug).\
            filter(PagesModel.deletetime == datetime_zero()).\
            filter(PagesModel.type == getattr(PagesType, pageType)).\
            first()
        if Page is None:
            abort(404, message="{type}(slug: {slug}) doesn't exist".format(type=pageType, slug=slug))
        return self.to_json(Page)

    def lists(self, pagesType):
        Pages = []
        query = PagesModel.query.\
            filter(PagesModel.deletetime == datetime_zero()).\
            filter(PagesModel.type == getattr(PagesType, pagesType)).\
            order_by(PagesModel.publishedtime).\
            all()
        for page in query:
            Pages.append(self.to_json(page))
        return Pages

    def update(self, pagesType, page_id):
        Page = PagesModel.query.get(page_id)
        if Page is None or Page.type != getattr(PagesType, pagesType):
            abort(404, message="{type}(id: {page_id}) doesn't exist".format(type=pagesType, page_id=page_id))

        parser = self.params().parse_args()
        pass_nones = ('publishedtime', 'deletetime', 'updatetime', )
        for key in parser:
            print(key, key in pass_nones, parser[key] is None)
            if key in ('createtime', 'id', ):
                continue

            if key in pass_nones and parser[key] is None:
                continue

            setattr(Page, key, parser[key])

        if Page.deletetime is None:
            Page.deletetime = datetime_zero()

        if Page.publishedtime is None:
            Page.publishedtime = Page.createtime

        db.session.commit()
        return self.to_json(PagesModel.query.get(page_id))

    def create(self, pagesType: str):
        params = self.params().parse_args()
        del params['id']
        Page = PagesModel()
        Page = init_from_dict(Page, params)

        db.session.add(Page)
        db.session.commit()
        return self.to_json(Page)

    def params(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('type', type=str)
        parser.add_argument('slug', type=str)
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('subtitle', type=str)
        parser.add_argument('author', required=True, type=int)
        parser.add_argument('content', type=str)
        parser.add_argument('publishedtime')
        parser.add_argument('deletetime', default=datetime_zero())
        parser.add_argument('updatetime', default=datetime_zero())
        parser.add_argument('createtime', default=datetime.utcnow())

        return parser

    def to_json(self, Pages: PagesModel):
        data = {
            'id': Pages.id,
            'type': Pages.type.value,
            'type_name': Pages.type.name,
            'slug': Pages.slug,
            'title': Pages.title,
            'subtitle': Pages.subtitle,
            'author': Pages.author,
            'content': Pages.content,
            'publishedtime': Pages.publishedtime,
            'deletetime': Pages.deletetime,
            'updatetime': Pages.updatetime,
            'createtime': Pages.createtime,
        }

        for t in ['publishedtime', 'deletetime', 'updatetime', 'createtime']:
            if datetime.timestamp(data[t]) == 0:
                data[t] = 0
            else:
                data[t] = data[t].isoformat()

        return data


@api.resource('/pages/')
class PagesWithoutId(Resource):
    def get(self):
        pdo = PagesDataObject()
        return pdo.lists('page')

    def post(self):
        pdo = PagesDataObject()
        return pdo.create('page')


@api.resource('/posts/')
class PostsWithoutId(Resource):
    def get(self):
        pdo = PagesDataObject()
        return pdo.lists('post')

    def post(self):
        pdo = PagesDataObject()
        return pdo.create('post')


@api.resource('/pages/<string:slug>')
class PagesWithSlug(Resource):
    def get(self, slug):
        pdo = PagesDataObject()
        return pdo.get_by_slug('page', slug)


@api.resource('/posts/<string:slug>')
class PostsWithSlug(Resource):
    def get(self, slug):
        pdo = PagesDataObject()
        return pdo.get_by_slug('post', slug)


@api.resource('/pages/<int:page_id>')
class Pages(Resource):
    def get(self, page_id):
        pdo = PagesDataObject()
        return pdo.get_by_id('page', page_id)

    def delete(self, page_id):
        pdo = PagesDataObject()
        return pdo.delete_by_id('page', page_id)

    def put(self, page_id):
        pdo = PagesDataObject()
        return pdo.update('page', page_id)


@api.resource('/posts/<int:page_id>')
class Posts(Resource):
    def get(self, page_id):
        pdo = PagesDataObject()
        return pdo.get_by_id('post', page_id)

    def delete(self, page_id):
        pdo = PagesDataObject()
        return pdo.delete_by_id('post', page_id)

    def put(self, page_id):
        pdo = PagesDataObject()
        return pdo.update('post', page_id)
