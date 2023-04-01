from flask import Flask, request, make_response, redirect, session, abort
from flask_login import LoginManager
import sqlite3
import json
import sys
import secrets
import bcrypt
import datetime

import os
login_manager = LoginManager()

app = Flask(__name__)
app.secret_key ="5v6rvuuvtuvfue"

valid_tokens = []

cx = sqlite3.connect("test.db")
cu = cx.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS userdata(username, pwd_hash, sleepdata)")

    # insert values into a table cu.execute("insert into lang values (?, ?)", ("C", 1972))

    # execute a query and iterate over the result for row in cu.execute("select * from lang"):

cx.close()

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
        print(valid_tokens)
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
    print(request.cookies)
    print(session)
    if (session_auth(session)):
        data = request.json
        year, month, day = data["day"].split("-")
        date = datetime.date(year, month, day)
        date.weekday()
        print(request.json)
        return "", 200
    return "", 403

@app.route("/getUserSleepData", methods=["GET"])
def getUserSleepData():
    with open("users.json","r") as userFile:
        for i in userFile:
            if session['username'] == i["username"]:
                data = []
                for j in i["sleepData"]["raw"]:
                    year, month, day = j["sleepData"]["raw"]["day"].split("-")
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
                    dailyData = dict(hours = 24 - j["sleepData"]["raw"]["start"] + j["sleepData"]["raw"]["end"],
                                     day = day,
                                     awake = j["sleepData"]["raw"]["end"],
                                     asleep = j["sleepData"]["raw"]["start"])
                    data.append(dailyData)
                dataToBeSent = dict(data = data, weeksum = i["sleepData"]["weekSum"], username = i["username"])
                return dataToBeSent