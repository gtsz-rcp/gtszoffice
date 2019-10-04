from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from lib.app import app
from lib.app import api
from lib.db import db

import pages.models
import pages.api as PagesApi
import users.models
import users.api as UsersApi
import artists.models
import artists.api as ArtistsApi
import bibliography.models_bookpartners
import bibliography.models_books
import bibliography.api_bookpartners
import bibliography.api_books

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def run_server():
    app.run()


if __name__ == '__main__':
    manager.run()
