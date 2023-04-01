from flask import Flask, request, make_response, redirect, session, abort
from flask_login import LoginManager
import json
import secrets
import bcrypt
import datetime
import main

login_manager = LoginManager()

app = Flask(__name__)
app.secret_key ="5v6rvuuvtuvfue"

valid_tokens = []

def saveUser(name, hashed):
    with open("users.json", "r") as userFile:
        users = json.loads(userFile.read())
        with open("users.json", "w") as userFileW:
            newUser = {}
            newUser["username"] = name
            newUser["hash"] = hashed
            newUser["sleepData"] = "null"
            users.append(newUser)
            userFileW.write(json.dumps(users, indent=4))
        
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
        for user in users:
            if user["username"] == username:
                hashed = user["hash"]
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
        start = data["start"]
        end = data["end"]
        year, month, day = data["day"].split("-")
        date = datetime.date(int(year), int(month), int(day))
        weekday = date.weekday()+1
        username = session["username"]
        main.processUser(start, end, weekday, username, data)
        return "", 200
    return "", 403


@app.route("/getUserSleepData", methods=["GET"])
def getUserSleepData():
    with open("users.json","r") as userFile:
        users = json.load(userFile)
        for user in users:
            username = session["username"]
            if username == user["username"]:
                data = []
                for j in user["sleepData"]["raw"]:
                    year, month, day = j["day"].split("-")
                    date = datetime.date(int(year), int(month), int(day))
                    weekday = date.weekday()+1
                    if weekday == 1:
                        day = "monday"
                    elif weekday == 2:
                        day = "tuesday"
                    elif weekday == 3:
                        day = "wednesday"
                    elif weekday == 4:
                        day = "thursday"
                    elif weekday == 5:
                        day = "friday"
                    elif weekday == 6:
                        day = "saturday"
                    elif weekday == 7:
                        day = "sunday"
                    dailyData = dict(hours = 24 - j["start"] + j["end"],
                                     day = day,
                                     awake = j["end"],
                                     asleep = j["start"])
                    data.append(dailyData)
                dataToBeSent = dict(data = data, weeksum = user["sleepData"]["weekSum"], username = user["username"])
                return dataToBeSent
                
@app.route("/leaderboard", methods=["GET"])
def leaderboard():
    with open("users.json", "r") as userFile:
        currentUser = session["username"]
        users = json.load(userFile)
        finalData = {}
        formattedData = []
        for user in users:
            if user["username"] ==  currentUser:
                finalData["current"] = {
                        "username":user["username"],
                        "time":user["sleepData"]["weekSum"]
                    }
            else:
                if user["sleepData"] != "null":
                    formattedData.append(
                        {
                            "username":user["username"],
                            "time":user["sleepData"]["weekSum"]
                        }
                    )
        formattedData.sort(key = lambda x: x["time"])
        formattedData.reverse()
        finalData["others"] = formattedData
        return json.dumps(finalData)

    return ""

@app.route("/getUser", methods=["GET"])
def getUser():
    with open("users.json","r") as userFile:
       pass

