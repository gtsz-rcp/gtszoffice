from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from lib.app import app
from lib.app import api
from lib.db import db

import pages.models
import pages.api as PagesApi

api.add_resource(PagesApi.PagesWithoutId, '/pages/')
api.add_resource(PagesApi.Pages, '/pages/<int:page_id>')
api.add_resource(PagesApi.PagesWithSlug, '/pages/<string:slug>')
api.add_resource(PagesApi.PostsWithoutId, '/posts/')
api.add_resource(PagesApi.Posts, '/posts/<int:page_id>')
api.add_resource(PagesApi.PostsWithSlug, '/posts/<string:slug>')

import users.models
import users.api as UsersApi

api.add_resource(UsersApi.Users, '/users/')
api.add_resource(UsersApi.UsersWithId, '/users/<int:user_id>')
api.add_resource(UsersApi.UserLogin, '/auth/login')
api.add_resource(UsersApi.UserLogout, '/auth/logout')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def run_server():
    app.run()


if __name__ == '__main__':
    manager.run()
