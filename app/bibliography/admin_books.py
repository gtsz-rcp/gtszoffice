from flask_admin.contrib.sqla import ModelView
from .models_books import Books

class BooksModelView(ModelView):
    page_size = 50
    form_excluded_columns = ['updatetime', 'createtime']

    create_template = 'book_create.html'

    def get_form(self):
        form = super().get_form()
        form.custom_vars = 'hahah'
        return form


def BooksModelViewInstance(db):
    return BooksModelView(Books, db.session)