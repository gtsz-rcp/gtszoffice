from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from lib.app import app
from lib.admin import admin
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


@manager.option('-e', '--email', dest='email')
@manager.option('-p', '--password', dest='password')
@manager.option('-n', '--name', dest='name', default='super admin')
def add_superuser(email, password, name):
    from sqlalchemy.orm import sessionmaker
    from argon2 import PasswordHasher

    ph = PasswordHasher()
    userdata = users.models.Users()
    super_exists = users.models.Users.query.filter_by(type=getattr(users.models.UsersType, 'superuser')).all()
    if len(super_exists) > 0:
        return 'sueruser already exits'
    
    userdata.type = 'superuser'
    userdata.email = email
    userdata.name = name
    userdata.password = ph.hash(password)
    
    db.session.add(userdata)
    return db.session.commit()


@manager.command
def run_server():
    app.run()


if __name__ == '__main__':
    manager.run()
