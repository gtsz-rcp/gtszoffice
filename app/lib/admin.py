from .app import app
from .db import db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from pages.admin import PagesModelViewInstance
from artists.models import Artists
from users.models import Users
from bibliography.admin_books import BooksModelViewInstance

admin = Admin(app, name='gtszrcp', template_mode="bootstrap3")
admin.add_view(PagesModelViewInstance(db))
admin.add_view(BooksModelViewInstance(db))
admin.add_view(ModelView(Artists, db.session))
admin.add_view(ModelView(Users, db.session))