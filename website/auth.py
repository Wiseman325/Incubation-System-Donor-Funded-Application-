from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "YES!"

    return render_template('login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        phone_number = request.form.get('phoneNumber')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 5:
            flash('Email must be greater than 4 characters', category='error')
        elif len(first_name) < 3:
            flash('First name must be greater than 2 characters', category='error')
        elif len(last_name) < 3:
            flash('Last name must be greater than 2 characters', category='error')
        elif len(phone_number) < 10:
            flash('Phone number cannot be less than 10 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
        else:
            new_user = User(email=email ,first_name=first_name ,last_name=last_name, phone_number=phone_number, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            if user:
                if user.is_active:
                 login_user(user, remember=True)
            flash('Account created successfull' ,category='success')
            return redirect(url_for('views.home'))


    return render_template("sign_up.html", user=current_user)