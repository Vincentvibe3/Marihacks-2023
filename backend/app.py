from flask import Flask, request, make_response, redirect, session, abort
from flask_login import LoginManager
import json
import secrets
import bcrypt
import datetime

login_manager = LoginManager()

app = Flask(__name__)
app.secret_key ="5v6rvuuvtuvfue"

valid_tokens = []

def saveUser(name, hash):
    with open("users.json", "r") as userFile:
        users = json.loads(userFile.read())
        with open("users.json", "w") as userFileW:
            users[name] = hash
            userFileW.write(json.dumps(users))
        
def genToken():
    return secrets.token_urlsafe(16)

def hash_password(password):
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed.decode("utf-8")

def check_hash(password, hash_string):
    hashed, password = hash_string.split(":")
    return bcrypt.checkpw(password, hashed)

def login_auth(username, password):
    with open("users.json", "r") as userFile:
        users = json.loads(userFile.read())
        hashed = users[username]
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

def session_auth(session):
    if 'token' in session:
        token = session['token']
        # Check jwt
        if token in valid_tokens:
            return True
    return False


@app.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    if login_auth(username, password):
        session['username'] = request.form['username']
        token = genToken()
        session['token'] = token
        valid_tokens.append(session['token'])
        return redirect("http://127.0.0.1:5173/callback?loggedIn=true")
    return redirect("http://127.0.0.1:5173/login")


@app.route("/register", methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    session['username'] = username
    saveUser(username, hash_password(password))
    token = genToken()
    session['token'] = token
    valid_tokens.append(token)
    return redirect("http://127.0.0.1:5173/callback?loggedIn=true")

@app.route("/logout", methods=["GET"])
def logout():
    session.pop('username', None)
    session.pop('token', None)
    return redirect("http://127.0.0.1:5173/callback")

@app.route("/log", methods=["POST"])
def log():
    if (session_auth(session)):
        data = request.json
        year, month, day = data["day"].split("-")
        date = datetime.date(year, month, day)
        date.weekday()
        return "", 200
    return "", 403

@app.route("/log", methods=["GET"])
def leaderboard():
    return ""
    
@app.route("/getUser", methods=["GET"])
def getUser():
    with open("users.json","r") as userFile:
       
