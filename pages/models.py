import datetime
from lib.db import db


class Pages(db.Model):
    __table_name__ = "pages"
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String, length=64, nullable=True, unique=True)
    title = db.Column(db.String, length=255, nullable=False)
    subtitle = db.Column(db.String, length=255, nullable=True, default=None)
    author = db.Column(db.Integer, default=1)
    content = db.Column(db.UnicodeText)
    deletetime = db.Column(db.DateTime, default='')
    updatetime = db.Column(db.DateTime, default='', onupdate=datetime.now)
    createtime = db.Column(db.DateTime, default=datetime.now)
