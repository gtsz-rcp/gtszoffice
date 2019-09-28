from datetime import datetime
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import abort
from lib.db import db
from lib.db import datetime_zero
from .models import Pages as PagesModel
from .models import init_from_dict


def Pages_to_json(Pages: PagesModel):
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


def pageParser(reqparse):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int)
    parser.add_argument('type', type=str)
    parser.add_argument('slug', type=str)
    parser.add_argument('title', type=str, required=True)
    parser.add_argument('subtitle', type=str)
    parser.add_argument('author', required=True, type=int)
    parser.add_argument('content', type=str)
    parser.add_argument('publishedtime')
    parser.add_argument('deletetime')
    parser.add_argument('updatetime')
    parser.add_argument('createtime')

    return parser


class PagesWithoutId(Resource):
    def get(self):
        Pages = []
        query = PagesModel.query.filter(
            PagesModel != datetime_zero()
            ).order_by(PagesModel.publishedtime).all()
        for page in query:
            Pages.append(Pages_to_json(page))
        return Pages

    def put(self):
        parser = pageParser(reqparse)
        Page = PagesModel()
        params = parser.parse_args()
        Page = init_from_dict(Page, params)

        db.session.add(Page)
        db.session.commit()
        return Pages_to_json(Page)


class PagesWithSlug(Resource):
    def get(self, slug):
        Page = PagesModel.query.filter_by(slug=slug).first()
        if Page is None:
            abort(404, message="Page(slug: {}) doesn't exist".format(slug))
        return Pages_to_json(Page)


class Pages(Resource):
    def get(self, page_id):
        Page = PagesModel.query.get(page_id)
        if Page is None:
            abort(404, message="Page(id: {}) doesn't exist".format(page_id))
        return Pages_to_json(Page)

    def delete(self, page_id):
        Page = PagesModel.query.get(page_id)
        if Page is None:
            abort(404, message="Page(id: {}) doesn't exist".format(page_id))

        Page.deletetime = datetime_zero()
        db.session.commit()
        return {'message': 'Page(id: {}) deleted'.format(page_id)}

    def put(self, page_id):
        Page = PagesModel.query.get(page_id)
        if Page is None:
            abort(404, message="Page(id: {}) doesn't exist".format(page_id))

        parser = pageParser(reqparse).parse_args()
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
        return Pages_to_json(PagesModel.query.get(page_id))
