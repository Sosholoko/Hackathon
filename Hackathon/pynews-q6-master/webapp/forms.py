import flask_wtf
import wtforms
from wtforms import validators as vld

# Form class --> flask_wtf.FlaskForm
# Form fields --> wtforms.SomethingField

# each form is a class inheriting from flask_wtf.FlaskForm
# every class attribute is a field in the form

class QueryForm(flask_wtf.FlaskForm):

    query = wtforms.StringField("Query: ", validators=[vld.DataRequired(message="Input something..")])

    submit = wtforms.SubmitField("Search")


class SignUpForm(flask_wtf.FlaskForm):
    
    mail = wtforms.StringField("Email", validators=[vld.Length(8, 50)])
    username = wtforms.StringField("Username ")
    password = wtforms.PasswordField("Password (Minimum of 6 characters)", validators=[vld.Length(6, 24)])
    confirm = wtforms.PasswordField("Repeat Password")
    

    submit = wtforms.SubmitField("Sign up →")


class SignInForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username ")
    password = wtforms.PasswordField("Password ", validators=[vld.Length(6, 24)])

    submit = wtforms.SubmitField("Connect →")


class Candidate(flask_wtf.FlaskForm):
    sexe = wtforms.StringField("Sexe ", validators=[vld.Length(1, 15)])
    firstname = wtforms.StringField("First Name ", validators=[vld.Length(1, 30)])
    lastname = wtforms.StringField("Last Name ", validators=[vld.Length(1, 30)])
    image = wtforms.FileField("Picture Profile") 
    age = wtforms.StringField("Age ", validators=[vld.Length(1, 3)])
    mail = wtforms.StringField("Mail ", validators=[vld.Length(5, 30)])
    height = wtforms.StringField("Height ", validators=[vld.Length(1, 3)])
    location = wtforms.StringField("City ", validators=[vld.Length(1, 30)])
    phone = wtforms.StringField("Phone Number ", validators=[vld.Length(1, 10)])
    nationality = wtforms.StringField("Nationality ", validators=[vld.Length(1, 30)])
    origin = wtforms.StringField("Origin ", validators=[vld.Length(1, 30)])
    father_job = wtforms.StringField("Father Situation ")
    mother_job = wtforms.StringField("Mother Situation ")
    father_origin = wtforms.StringField("Father Origin ")
    mother_origin = wtforms.StringField("Mother Origin ")
    school = wtforms.StringField("School ")
    future_job = wtforms.StringField("Future Situation ", validators=[vld.Length(1, 30)])
    eye_color = wtforms.StringField("Eye Color ", validators=[vld.Length(1, 30)])
    hair_color = wtforms.StringField("Hair Color ", validators=[vld.Length(1, 30)]) 
    body =  wtforms.StringField("Body Size ", validators=[vld.Length(1, 30)])
    religion = wtforms.StringField("Religion Level ", validators=[vld.Length(1, 30)])
    torah = wtforms.StringField("Limud Torah ", validators=[vld.Length(1, 30)])
    jew_status = wtforms.StringField("Jewish Status ", validators=[vld.Length(1, 30)])
    sexe_1 = wtforms.StringField("Wanted Sexe ", validators=[vld.Length(1, 30)])
    eye_color_1 = wtforms.StringField("Wanted Eye Color ", validators=[vld.Length(1, 30)])
    hair_color_1 = wtforms.StringField("Wanted Hair Color ", validators=[vld.Length(1, 30)]) 
    body_1 =  wtforms.StringField("Wanted Body Size ", validators=[vld.Length(1, 30)])
    religion_1 = wtforms.StringField("Wanted Religion Level ", validators=[vld.Length(1, 30)])
    torah_1 = wtforms.StringField("Wanted Limude Torah  ", validators=[vld.Length(1, 30)])
    jew_status_1 = wtforms.StringField("Wanted Jewish Status ", validators=[vld.Length(1, 30)])

    submit = wtforms.SubmitField("Validate")

