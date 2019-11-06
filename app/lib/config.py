import os
import sys

DEBUG = True
ENV = 'development'
SECRET_KEY = "ZF>)?6Sj{TSI<9`zRUc>6hT>ycfXOL"
APPLICATION_ROOT = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
EXPLAIN_TEMPLATE_LOADING = False

SQLALCHEMY_DATABASE_URI = 'postgresql://gtszoffice:gtszoffice@localhost/gtszoffice'
SQLALCHEMY_TRACK_MODIFICATIONS = True

FLASK_ADMIN_SWATCH = 'cerulean'