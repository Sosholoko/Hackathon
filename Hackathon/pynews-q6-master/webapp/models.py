# MODELS.py
from . import db, login_manager # Database bridge created in __init__.py
import flask_login

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


# user2candidate = db.Table(
#     "user2candidate", # name of the table
#     db.Column("user_id", db.Integer(), db.ForeignKey("user.id"), primary_key=True),
#     db.Column("candidate_id", db.Integer(), db.ForeignKey("candi.id"), primary_key=True),
# ) # PK will be a combination of the two (1-2)



class User(db.Model, flask_login.UserMixin): 

    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)

    mail = db.Column(db.String(64), nullable=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))
    boolean = db.Column(db.Boolean, default=False)
    new_candidate = db.relationship("Candidate")

    # new_candidate = db.relationship("Candidate", backref="user", secondary=user2candidate)

class Candidate(db.Model):
    __tablename__ = 'candi'
    id = db.Column(db.Integer(), primary_key = True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id')) 

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

    def delete(self):
        db.session.delete(self)
        db.session.commit()







