from flask import render_template, Blueprint, request, redirect, url_for,jsonify
from flask_login import login_required, current_user
from .models import Books
 


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/profile')
@login_required
def profile():
    user = current_user
    bookQuery = Books.query.all()
    return render_template('profile.html', name=user.username, booksToDisplay=bookQuery)


@main.route('/profile', methods=['POST'])
@login_required
def profilePost():
    user = current_user
    wordToSearch = request.form.get('wordToSearch')
    wordFormated = f"{wordToSearch}%"
    bookQuery = Books.query.filter(Books.title.ilike(wordFormated) | Books.author.ilike(
        wordFormated) | Books.isbn.ilike(wordFormated)).all()
    return render_template('profile.html', name=user.username, booksToDisplay=bookQuery)

