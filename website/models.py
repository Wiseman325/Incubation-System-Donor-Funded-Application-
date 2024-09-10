from . import db
from flask_login import UserMixin;

class Student(db.Model, UserMixin):
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
    course_id = db.Column(db.Integer, db.ForeignKey('Course._id'), nullable=False)


class Course(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))
    duration = db.Column(db.Integer(80))
    cost = db.Column(db.Integer(80))
    student_id = db.relationship('Student')

class Donor(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phoneNumber = db.Column(db.String(80))
    organisation = db.Column(db.String(80))
    amount = db.Column(db.Integer(80))
    payment_id = db.relationship('Payment')
    certificate_id = db.relationship('Certificate')


class Certificate(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    issuedDate = db.Column(db.Date)
    message = db.Column(db.String(80))
    signiture = db.Column(db.String(80))
    donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)


class Payment(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.Date)
    paymentMethod = db.Column(db.String(100))
    donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)

class FinancialAid(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student._id'), nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)
    application_status = db.Column(db.String(100))
    application_date = db.Column(db.Date)


