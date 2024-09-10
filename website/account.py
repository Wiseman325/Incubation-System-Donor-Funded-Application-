from flask import Blueprint, render_template, request
from . import db

account = Blueprint('account', __name__)

@account.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "YES!"

    return render_template('login.html')

@account.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        idNumber = request.form.get('idNumber')
        email = request.form.get('email')
        race = request.form.get('race')
        nationality = request.form.get('nationality')
        phoneNumber = request.form.get('phoneNumber')
        emailAddress = request.form.get('emailAddress')
        physicalAddress = request.form.get('physicalAddress')
        highestGrade = request.form.get('highestGrade')
        financialStatus = request.form.get('financialStatus')

        new_student = Student()
        new_student.name = name
        new_student.surname = surname
        new_student.idNumber = idNumber
        new_student.emailAddress = email
        new_student.race = race
        new_student.nationality = nationality
        new_student.phoneNumber = phoneNumber
        new_student.emailAddress = emailAddress
        new_student.physicalAddress = physicalAddress
        new_student.highestGrade = highestGrade
        new_student.financialStatus = financialStatus

        db.session.add(new_student)
        db.session.commit()
        return "YES!"

    return render_template('signup.html')