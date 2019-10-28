from datetime import datetime
from lib.db import db
from users.models import Users


class Artists(db.Model):
    __table_name__ = 'artist'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    name_en = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=True)
    user = db.relationship('Users', backref='artists', lazy=True)
    place = db.Column(db.String(16), nullable=True)
    updatetime = db.Column(
        db.DateTime,
        nullable=True,
        onupdate=datetime.utcnow()
        )
    createtime = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f"{self.name}({self.place})"
