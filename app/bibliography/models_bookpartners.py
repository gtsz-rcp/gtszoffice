import enum
from datetime import datetime
from lib.db import db
from lib.db import datetime_zero
from artists.models import Artists


class BookPartnerType(enum.Enum):
    writer = 1
    editor = 2
    designer = 3
    artist = 4

    def label(self):
        return self.name


class BookPartners(db.Model):
    __table_name__ = 'book_partners'

    id = db.Column(db.Integer(), primary_key=True)
    order = db.Column(db.Integer(), default=0)
    type = db.Column(
        db.Enum(BookPartnerType),
        nullable=False,
        default='artist')
    artist_id = db.Column(
        db.Integer(), 
        db.ForeignKey('artists.id'))
    artist = db.relationship(
        'Artists', 
        backref='book_partners', 
        lazy=True)
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
