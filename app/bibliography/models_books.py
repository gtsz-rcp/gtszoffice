import enum
from datetime import datetime
from lib.db import db
from lib.db import datetime_zero


class Colorspace(enum.Enum):
    CMYK = 1
    RGB = 2
    GRAY = 3
    BNW = 4

    def label(self):
        label_dict = {
            'GRAY': 'Grayscale',
            'BNW': 'Black And White'
        }

        if self.name in label_dict:
            return label_dict[self.name]
        return self.name


class Books(db.Model):
    __table_name__ = 'books'

    id = db.Column(db.Integer(), primary_key=True)
    slug = db.Column(db.String(64), nullable=False, unique=True)
    title = db.Column(db.String(255), nullable=False)
    subtitle = db.Column(db.String(255), nullable=True)
    language = db.Column(
        db.String(10),
        nullable=False,
        default='ko',
        doc='language type as i18n format')
    place = db.Column(
        db.String(16),
        nullable=False,
        default="Seoul",
        doc='the place the book published')
    medium = db.Column(db.String(64), nullable=True)
    page_amt = db.Column(db.Integer(), nullable=True)
    binding = db.Column(db.String(64), nullable=True)
    colorspace = db.Column(
        db.Enum(Colorspace),
        nullable=False,
        default='CMYK')
    summary = db.Column(db.UnicodeText, nullable=True)
    toc = db.Column(db.UnicodeText, nullable=True)
    publishedtime = db.Column(db.DateTime, nullable=False)
    updatetime = db.Column(
        db.DateTime,
        nullable=True,
        default=datetime_zero())
    createtime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow())
