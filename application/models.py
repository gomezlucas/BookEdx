from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(50))


class Books(UserMixin, db.Model):
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    book_id = db.Column(db.Integer, primary_key=True)
    isbn  = db.Column(db.String(10))
    year = db.Column(db.Integer)

