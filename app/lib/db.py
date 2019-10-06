from datetime import datetime
from .app import app
from flask_sqlalchemy import SQLAlchemy


def datetime_zero():
    return datetime.fromtimestamp(0)


db = SQLAlchemy(app)
