# IMPORTS
from flask import Flask, Blueprint, render_template, url_for, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from secrets import token_hex


# GLOBALS
DB_NAME = "app.db"

# BLUEPRINTS

# SETUP
app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
db = SQLAlchemy(app)


# MODELS
class Student(db.Model, UserMixin):
    _id = db.Column(db.Integer, primary_key=True)
    idNumber = db.Column(db.String(13))
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    race = db.Column(db.String(80))
    nationality = db.Column(db.String(80))
    phoneNumber = db.Column(db.String(80))
    emailAddress = db.Column(db.String(120))
    physicalAddress = db.Column(db.String(80))
    highestGrade = db.Column(db.String(80))
    financialStatus = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    # course_id = db.Column(db.Integer, db.ForeignKey('Course._id'), nullable=False)

class Course(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(80))
    duration = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    # student_id = db.relationship('Student')

class Donor(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phoneNumber = db.Column(db.String(80))
    organisation = db.Column(db.String(80))
    amount = db.Column(db.Integer)
    # payment_id = db.relationship('Payment')
    # certificate_id = db.relationship('Certificate')


class Certificate(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    issuedDate = db.Column(db.Date)
    message = db.Column(db.String(80))
    signiture = db.Column(db.String(80))
    # donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)


class Payment(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.Date)
    paymentMethod = db.Column(db.String(100))
    # donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)

class FinancialAid(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    # student_id = db.Column(db.Integer, db.ForeignKey('student._id'), nullable=False)
    # donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)
    application_status = db.Column(db.String(100))
    application_date = db.Column(db.Date)


# CODE
@app.route('/home')
def home():
    return "<h2>Velkom</h2>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form.get('usernameOrEmail')
        password = request.form.get('password')

        userByUsername = Student.query.filter_by(username=username_or_email, password=password).first()
        userByEmail = Student.query.filter_by(emailAddress=username_or_email, password=password).first()
        
        print(userByEmail, userByUsername, username_or_email, password)
        if userByUsername or userByEmail:
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid username or password.")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        idNumber = request.form.get('idNumber')
        race = request.form.get('race')
        nationality = request.form.get('nationality')
        phoneNumber = request.form.get('phoneNumber')
        emailAddress = request.form.get('emailAddress')
        physicalAddress = request.form.get('physicalAddress')
        highestGrade = request.form.get('highestGrade')
        financialStatus = request.form.get('financialStatus')
        username = request.form.get('username')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        new_student = Student()
        new_student.name = name
        new_student.surname = surname
        new_student.idNumber = idNumber
        new_student.emailAddress = emailAddress
        new_student.race = race
        new_student.nationality = nationality
        new_student.phoneNumber = phoneNumber
        new_student.physicalAddress = physicalAddress
        new_student.highestGrade = highestGrade
        new_student.financialStatus = financialStatus
        new_student.username = username
        new_student.password = password

        if len(idNumber) != 13:
            return render_template('signup.html', error="ID Number must be 13 digits. Try Again!")
        if password != confirmPassword:
            return render_template('signup.html', error="Password Do Not Match. Try Again!")

        print(new_student.__dict__)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
