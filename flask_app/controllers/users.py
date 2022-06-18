from crypt import methods
from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models import user

#Create Route Controller 
@app.route("/create/user", methods=["POST"])
def creating_user():
    if user.User.create_user(request.form):
        return redirect('/users/profile')
    return redirect ("/")

#Read Route Controller
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/users/profile")
def user_profile():
    this_user = user.User.get_user_by_id(session['user_id'])
    return render_template("profile.html" , this_user=this_user)

@app.route("/users/login", methods=['POST'])
def login(): 
    if user.User.login(request.form): 
        return redirect("/users/profile")
    return redirect('/')
    
#Update Route Controller

#Delete Route Controller 
@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
