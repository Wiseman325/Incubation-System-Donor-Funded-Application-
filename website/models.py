from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    _id = db.Column(db.Integer, primary_key=True)
    id_number = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) 
    race = db.Column(db.String(80))
    nationality = db.Column(db.String(80))
    phone_number = db.Column(db.String(80))
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    physical_address = db.Column(db.String(80))
    highest_grade = db.Column(db.String(80))
    financial_status = db.Column(db.String(80))
    course_id = db.Column(db.Integer, db.ForeignKey('course._id'), nullable=False)

class Course(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80))
    duration = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    students = db.relationship('User', backref='course', lazy=True)

class Donor(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80))
    organisation = db.Column(db.String(80))
    amount = db.Column(db.Integer)
    payments = db.relationship('Payment', backref='donor', lazy=True)
    certificates = db.relationship('Certificate', backref='donor', lazy=True)

class Certificate(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    issue_date = db.Column(db.Date)
    message = db.Column(db.String(80))
    signature = db.Column(db.String(80))
    donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)

class Payment(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.Date)
    payment_method = db.Column(db.String(100))
    donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)

class FinancialAid(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user._id'), nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)
    application_status = db.Column(db.String(100))
    application_date = db.Column(db.Date)
