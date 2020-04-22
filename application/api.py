from flask import render_template, Blueprint, jsonify
from .models import Review, Books 

api = Blueprint('api', __name__)


@api.route('/api/<string:isbn>')
def apifunc(isbn):  

    booksQuery = Books.query.filter_by(isbn=isbn).first()
    
    if booksQuery is None:
        return jsonify({'error': 'Invalid ISBN'}), 404

    reviewsCount= Review.query.filter_by(book_id=booksQuery.book_id).count()

    if reviewsCount > 0:
        reviews = Review.query.filter_by(book_id=booksQuery.book_id)
        result = 0
        for  review in reviews:
            result = result + review.score
            average = result / reviewsCount
    else:
        average = 0
    
    return jsonify({
        'title': booksQuery.title, 
        'author': booksQuery.author,
        'year': booksQuery.year,
        'isbn': booksQuery.isbn,
        'review_count': reviewsCount,
        'average_score': average
    })