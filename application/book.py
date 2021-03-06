import os
import requests
from flask import render_template, Blueprint, request, redirect, url_for, flash
from .models import Books, Review, User
from datetime import datetime
from flask_login import login_required, current_user
from . import db


book = Blueprint("book", __name__)

@book.route('/book/<string:isbn>')
@login_required
def index(isbn):

   bookInfo = Books.query.filter_by(isbn=isbn).first()
   responseGoodReviews = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": os.getenv("API_KEY"), "isbns": isbn})
   
   if bookInfo is None or responseGoodReviews.status_code == "404" :
      return render_template("errorPage.html")

   goodReviews = responseGoodReviews.json()
   goodReviews = goodReviews['books'][0]
   book = Books.query.filter_by(isbn=isbn).first()

   userReview = Review.query.filter(Review.user_id == current_user.id, Review.book_id==bookInfo.book_id).first()
   allReviews = db.session.query(User, Review).outerjoin(Review, User.id == Review.user_id).filter(Review.book_id == bookInfo.book_id, Review.user_id != current_user.id).order_by(Review.timestamp.desc()).all()

   return render_template('book.html', bookInfo=bookInfo , goodReviews=goodReviews, userReview=userReview, allReviews=allReviews )


@book.route('/book/<string:isbn>', methods=["POST"])
@login_required
def bookPost(isbn):
 
   score = request.form.get('inlineRadioOptions')
   reviewText = request.form.get('reviewText')
   dt = datetime.now()
   user = current_user.id
   book = Books.query.filter_by(isbn=isbn).first()

   reviewCount = Review.query.filter(Review.user_id == current_user.id , Review.book_id == book.book_id).count()
   if reviewCount > 0:
      new_review = Review.query.filter(Review.user_id == current_user.id , Review.book_id == book.book_id).first()
      new_review.score = score 
      new_review.timestamp = dt
      new_review.review_text = reviewText
   else:
      new_review = Review(review_text=reviewText, score=score, timestamp = dt, user_id=user, book_id=book.book_id )
      db.session.add(new_review)

   db.session.commit()
   
   return redirect(url_for("book.index", isbn=book.isbn))
 