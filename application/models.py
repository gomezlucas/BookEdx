from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    username = db.Column(db.String(50))
    reviews = db.relationship('Review', backref="user")


class Books(UserMixin, db.Model):
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    book_id = db.Column(db.Integer, primary_key=True)
    isbn  = db.Column(db.String(10))
    year = db.Column(db.Integer)
 
class Review(UserMixin, db.Model):
    __tablename__ = 'reviews'
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer,db.ForeignKey('books.book_id'))
    review_text  = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime)
    score= db.Column(db.Integer)
 


