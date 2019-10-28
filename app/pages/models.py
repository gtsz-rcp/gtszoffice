import enum
from datetime import datetime
from lib.db import db
from lib.db import datetime_zero
from artists.models import Artists


class PagesType(enum.Enum):
    page = 1
    post = 2


class Pages(db.Model):
    __table_name__ = "pages"

    id = db.Column(db.Integer(), primary_key=True)
    type = db.Column(db.Enum(PagesType), nullable=False, default='post')
    slug = db.Column(db.String(64), nullable=True, unique=True)
    title = db.Column(db.String(255), nullable=False)
    subtitle = db.Column(db.String(255), nullable=True, default=None)
    author_id = db.Column(db.Integer(), db.ForeignKey('artists.id'))
    author = db.relationship('Artists', backref='pages', lazy=True)
    content = db.Column(db.UnicodeText)
    publishedtime = db.Column(db.DateTime, default=datetime.now())
    deletetime = db.Column(db.DateTime, nullable=True, default=None)
    updatetime = db.Column(db.DateTime, nullable=True, default=datetime_zero(), onupdate=datetime.utcnow())
    createtime = db.Column(db.DateTime, default=datetime.now())


def init_from_dict(Pages: Pages, params: dict):
    for key in params:
        if key not in params or params[key] is None:
            continue
        setattr(Pages, key, params[key])

    return Pages
