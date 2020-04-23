from flask import render_template, Blueprint, request, redirect, url_for, flash, session
from .models import User
from flask_login import login_user, logout_user, login_required,  current_user
from . import db
from  werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    if  current_user.is_anonymous:
        return render_template('login.html')
    else:
        return redirect(url_for('main.profile'))



@auth.route('/login', methods=['POST'])
def loginPost():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        login_user(user, remember = remember)
        return redirect(url_for('main.profile'))
    flash("Login failed: Invalid username or password", "danger")
    return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signupPost():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')

    user = User.query.filter_by(email=email).first()
   
    if user:
        flash("Email already exists! Try another one", "danger")
        return redirect(url_for('auth.signup'))
    
    if password != confirmPassword:
        flash("The passwords doesn't match. Please try again!", "danger")
        return redirect(url_for('auth.signup'))

    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(email=email, username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    flash(" Your account has been created! You can log in now", "success")
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))