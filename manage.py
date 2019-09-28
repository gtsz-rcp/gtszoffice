from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from lib.app import app
from lib.app import api
from lib.db import db

from pages.models import *
from pages.api import PagesWithoutId
from pages.api import Pages
from pages.api import PagesWithSlug

api.add_resource(PagesWithoutId, '/pages/')
api.add_resource(Pages, '/pages/<int:page_id>')
api.add_resource(PagesWithSlug, '/pages/<string:slug>')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def run_server():
    app.run()


if __name__ == '__main__':
    manager.run()
