import enum
from datetime import datetime
from lib.db import db
from lib.db import datetime_zero


class BookPartnerType(enum.Enum):
    writer = 1
    editor = 2
    designer = 3
    artist = 4

    def label(self):
        label_dict = {
            'writer': 'Writer',
            'editor': 'Editor',
            'designer': 'Designer',
            'artist': 'Artist'
        }

        return label_dict[self.name]


class BookPartnerTypeLabel(enum.Enum):
    writer = (1, 'Writer')
    editor = (2, 'editor')
    designer = (3, 'designer')
    artist = (4, 'artist')

class BookPartners(db.Model):
    __table_name__ = 'book_writers'

    id = db.Column(db.Integer(), primary_key=True)
    order = db.Column(db.Integer(), default=0)
    type = db.Column(
        db.Enum(BookPartnerType),
        nullable=False,
        default='artist')
    artist = db.Column(
        db.Integer(),
        nullable=False,
        doc='foreign with artists')
    book = db.Column(
        db.Integer(),
        nullable=False,
        doc='foreign with books')
    updatetime = db.Column(
        db.DateTime,
        nullable=True,
        default=datetime_zero(),
        onupdate=datetime.utcnow())
    createtime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime_zero())
