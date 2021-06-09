import flask
from flask import request, jsonify
from flask_socketio import SocketIO, emit, send
from . import app       # . is webapp/
from . import forms, models, db, mail_functions
import flask_login
from flask_login import login_user, current_user, logout_user, login_required, login_manager
import pusher
import json
from time import localtime, strftime
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects



socketio = SocketIO(app, cors_allowed_origins="*")

pusher_client = pusher.Pusher(
    app_id='1190483',
    key='9282a2def65164d7d0bb',
    secret='5f43b399aac7287fd054',
    cluster='ap2',
    ssl=True
)

@app.route("/test")
def test():
    flask.flash("Testing mail sending !")

    mail_functions.send_mail(title="Hello world",
                            body="This is a test !",
                            recipients="sashakharoubi@gmail.com",
                            html=flask.render_template('mail.html', body="Hello World !")
                            )

    return flask.redirect('/')

@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/add", methods=["GET","POST"])
def addnew():
    form = forms.Candidate()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            sexe = form.sexe.data
            firstname = form.firstname.data
            lastname = form.lastname.data
            mail = form.mail.data
            age = form.age.data
            height = form.height.data
            location = form.location.data
            phone = form.phone.data
            nationality = form.nationality.data
            origin = form.origin.data
            father_job = form.father_job.data
            mother_job = form.mother_job.data
            father_origin = form.father_origin.data
            mother_origin = form.mother_origin.data
            school = form.school.data
            future_job = form.future_job.data
            eye_color = form.eye_color.data
            hair_color = form.hair_color.data
            body = form.body.data
            religion = form.religion.data 
            torah = form.torah.data
            jew_status = form.jew_status.data
            sexe_1 = form.sexe_1.data
            eye_color_1 = form.eye_color_1.data
            hair_color_1 = form.hair_color_1.data
            body_1 = form.body_1.data
            religion_1 = form.religion_1.data 
            torah_1 = form.torah_1.data
            jew_status_1 = form.jew_status_1.data
            # image = form.image.data
                    
            newCandidate = models.Candidate(firstname=firstname, lastname=lastname, age=age,height=height,location=location,
                                    phone=phone, nationality=nationality,origin=origin, father_job=father_job,
                                    mother_job=mother_job, father_origin=father_origin, mother_origin=mother_origin,
                                    school=school,mail=mail, future_job=future_job, eye_color=eye_color,hair_color=hair_color,
                                    body=body, religion=religion, torah=torah, jew_status=jew_status, eye_color_1=eye_color_1,hair_color_1=hair_color_1,
                                    body_1=body_1, religion_1=religion_1, torah_1=torah_1, jew_status_1=jew_status_1, sexe=sexe, sexe_1=sexe_1 )
            
            flask_login.current_user.new_candidate.append(newCandidate)
            db.session.add(newCandidate)
            db.session.commit()
            flask.flash("You added a new candidate to your list", "success")
            
        else:
            flask.flash("You haven't fill the entire form correctly, try again !", "danger")
    
    return flask.render_template("candidate.html", form=form)

# firstname=firstname, lastname=lastname, age=age,height=height,location=location,
#                                 phone=phone, nationality=nationality,origin=origin, father_job=father_job,
#                                 mother_job=mother_job, father_origin=father_origin, mother_origin=mother_origin,
#                                 school=school, future_job=future_job)




@app.route("/candi/<int:candi_id>/request")
def comparing(candi_id):
    mycandis = models.Candidate.query.get(candi_id)
    requestcandi1 = models.Candidate.query.filter_by(eye_color = mycandis.eye_color_1, hair_color = mycandis.hair_color_1, 
                                                    body = mycandis.body_1, religion = mycandis.religion_1, torah= mycandis.torah_1,
                                                    jew_status= mycandis.jew_status_1, sexe = mycandis.sexe_1).all()
    requestcandibase = models.Candidate.query.filter_by( sexe = mycandis.sexe_1).all()
    requestcandiphybase = models.Candidate.query.filter_by( sexe = mycandis.sexe_1, body = mycandis.body_1, eye_color = mycandis.eye_color_1).all()
    requestcandiphytot = models.Candidate.query.filter_by( sexe = mycandis.sexe_1, body = mycandis.body_1, eye_color = mycandis.eye_color_1, hair_color = mycandis.hair_color_1).all()
    requestcandirel = models.Candidate.query.filter_by( sexe = mycandis.sexe_1, torah = mycandis.torah_1, religion = mycandis.religion_1, jew_status = mycandis.jew_status_1).all()
    requestcandibaserel = models.Candidate.query.filter_by( sexe = mycandis.sexe_1, religion = mycandis.religion_1, jew_status = mycandis.jew_status_1).all()
    return flask.render_template("result.html", requestcandi1 = requestcandi1, requestcandibase=requestcandibase, requestcandiphybase = requestcandiphybase, requestcandiphytot =requestcandiphytot, requestcandirel = requestcandirel,requestcandibaserel=requestcandibaserel, mycandis= mycandis )
    


@app.route("/candi")
def candi_list():
    candiss = models.Candidate.query.all()
    print(candiss)
    candis = flask_login.current_user.new_candidate
    print(candis)
    return flask.render_template("candi_list.html", candis=candis)

@app.route("/candi/<int:candi_id>")
def candi_page(candi_id):
    candi = models.Candidate.query.get(candi_id)
    return flask.render_template("candi_page.html", candi=candi)

@socketio.on('message')
def handleMessage(data):
    
    send(data)
    

@app.route("/messages")
def messages():

    all_users = models.User.query.filter_by(boolean=True)
    return flask.render_template("messages.html", all_users = all_users )

@app.route('/message', methods=['POST'])
def message():

    try:

        username = request.form.get('username')
        message = request.form.get('message')
        print(username)

        # new_message = Message(username=username1, message=message1)
        # db.session.add(new_message)
        # db.session.commit()

        pusher_client.trigger('chat-channel', 'new-message', {'username' : username, 'message': message, 'time_stamp': strftime('%b-%d %I:%M%p', localtime())})

        return jsonify({'result' : 'success'})
    
    except:

        return jsonify({'result' : 'failure'})



@app.route("/sign-up", methods=["GET","POST"])
def signup():
    form = forms.SignUpForm()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            mail     = form.mail.data

            new_user = models.User(name = username, password = password, mail=mail)
            db.session.add(new_user)
            db.session.commit()
            mail_functions.send_mail(title="Welcome" +" "+ new_user.name ,
                            body="This is a test !",
                            recipients=new_user.mail,
                            html=flask.render_template('mail.html', body="Welcome to Match UP, your new account "
                                                                        " is set up ! You're good to go. You can now "
                                                                        " sign in into your account and start working ! "
                                                                        " Enjoy !")
                            )
            return flask.redirect('/sign-in')

        else:
            flask.flash("You haven't fill up the forms properly ! Please try again", "danger")

    
    
    return flask.render_template("signup.html", form=form)

#Route to display a list of the users registered

@app.route("/users")
def users_list():
    users = models.User.query.all()
    return flask.render_template("users_list.html", users=users)


#Route for profile

@app.route("/users/<int:user_id>")
def profile_page(user_id):
    user = models.User.query.get(user_id)
    return flask.render_template("user_page.html", user=user)



@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    
    form = forms.SignInForm()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
    
            # Retrieve the user that matches this username
            user = models.User.query.filter_by(name=username).first()
            print(user.boolean)

            # Check the provided password against the user's one
            if user is not None and user.password == password:
                flask_login.login_user(user)
                flask.flash(f"{user.name} logged in successfully !", "success")
                idn = user.id
                user.boolean = True
                db.session.commit()
                print(user.boolean)
                return flask.render_template('user_page.html', user=user)
            else:
                flask.flash("Something went wrong.", "danger") # Put the message into the flashed messages
                # To retrieve those messages: flask.get_flashed_messages()

    return flask.render_template("signin.html", form=form)

@app.route("/sign-out", methods=["GET"])
def signout():
    
    all_users = models.User.query.all()
    
    for user in all_users:
        if user.boolean == True:
            user.boolean = False
            print(user.boolean)
            db.session.commit() 
            print('OK')
            flask_login.logout_user()
            flask.flash("You successfully logout !", "danger")
            return flask.redirect('/sign-in')
        else:
            pass


























