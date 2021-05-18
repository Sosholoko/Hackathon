# MODELS.py
from . import db, login_manager # Database bridge created in __init__.py
import flask_login

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)






class User(db.Model, flask_login.UserMixin): # db.Model is required if you want to create an SQL model

    # Every attribute is a class variable

    id = db.Column(db.Integer(), primary_key=True)

    mail = db.Column(db.String(64), nullable=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    boolean = db.Column(db.Boolean, default=False)

class Candidate(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    sexe = db.Column(db.String(15))
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    age = db.Column(db.Integer())
    mail = db.Column(db.String(64))
    height = db.Column(db.Integer())
    location = db.Column(db.String(64))
    phone = db.Column(db.Integer())
    nationality = db.Column(db.String(64))
    origin = db.Column(db.String(64))
    father_job = db.Column(db.String(64))
    mother_job = db.Column(db.String(64))
    father_origin = db.Column(db.String(64))
    mother_origin = db.Column(db.String(64))
    school = db.Column(db.String(64))
    future_job = db.Column(db.String(64))
    eye_color = db.Column(db.String(64))
    hair_color = db.Column(db.String(64))
    body = db.Column(db.String(64))
    religion = db.Column(db.String(64))
    torah = db.Column(db.String(64))
    jew_status = db.Column(db.String(64))
    sexe_1 = db.Column(db.String(64))
    eye_color_1 = db.Column(db.String(64))
    hair_color_1 = db.Column(db.String(64))
    body_1 = db.Column(db.String(64))
    religion_1 = db.Column(db.String(64))
    torah_1 = db.Column(db.String(64))
    jew_status_1 = db.Column(db.String(64))







