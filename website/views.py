
from flask import Blueprint, abort, jsonify, render_template, request, redirect, session, url_for, flash
from flask_login import login_required ,current_user
from .models import User
from . import db
from datetime import date, datetime

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")

@views.route('/admin')
def admin():
    admin_email = 'YouthAdmin@gmail.com'
    admin_password = 'YouthAdmin'
    if request.method == 'POST':
        if request.form['email'] == admin_email and request.form['password'] == admin_password:
            return redirect(url_for('admin_view'))
        else:
            flash('Invalid email or password')
    users = User.query.all()

    return render_template('admin_dashboard.html',users=users, user=current_user)