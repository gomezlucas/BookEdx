from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from .models import User
from flask_login import login_user, logout_user, login_required
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def loginPost():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    
    if user and password == user.password:
        login_user(user, remember = remember)
        return redirect(url_for('main.profile'))
    flash("Login failed: Invalid username or password")
    return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signupPost():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash("Email already exists! Try another one")
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('main.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))