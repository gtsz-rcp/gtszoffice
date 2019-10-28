from flask_admin.contrib.sqla import ModelView
from .models import Pages

class PagesModelView(ModelView):
    page_size = 50
    form_excluded_columns = ['createtime', 'updatetime', 'deletetime']
    form_ajax_refs = {
        'author': {
            'fields': ['name', 'name_en'],
            'page_size': 50
        }
    }
    column_exclude_list = ['deletetime', 'updatetime']

def PagesModelViewInstance(db):
    return PagesModelView(Pages, db.session)