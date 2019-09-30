import enum
from datetime import datetime
from lib.db import db


class UsersType(enum.Enum):
    user = 1
    admin = 100


class Users(db.Model):
    __table_name__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.Enum(UsersType), nullable=False, default='user')
    email = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(255), nullable=False, unique=True)
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
