from datetime import datetime
from lib.db import db


class Artists(db.Model):
    __table_name__ = 'artist'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    name_en = db.Column(db.String(64), nullable=False)
    user = db.Column(db.Integer(), nullable=True)
    place = db.Column(db.String(16), nullable=True)
    updatetime = db.Column(
        db.DateTime,
        nullable=True,
        onupdate=datetime.utcnow()
        )
    createtime = db.Column(db.DateTime, default=datetime.now())
