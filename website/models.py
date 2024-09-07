from . import create_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(create_app())

class Student(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    idNumber = db.Column(db.Integer)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    race = db.Column(db.String(80))
    nationality = db.Column(db.String(80))
    phoneNumber = db.Column(db.String(80))
    emailAddress = db.Column(db.String(120), unique=True)
    physicalAddress = db.Column(db.String(80))
    highestGrade = db.Column(db.String(80))
    financialStatus = db.Column(db.String(80))

class Course(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))
    duration = db.Column(db.Integer(80))
    cost = db.Column(db.Integer(80))

class Donor(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phoneNumber = db.Column(db.String(80))
    organisation = db.Column(db.String(80))
    amount = db.Column(db.Integer(80))


class Certificate(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    issuedDate = db.Column(db.Date)
    message = db.Column(db.String(80))
    signiture = db.Column(db.String(80))


class Payment(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.Date)
    paymentMethod = db.Column(db.String(80))



