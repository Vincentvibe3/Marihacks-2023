from flask import Flask, request, make_response, redirect, session, abort
from flask_login import LoginManager
import sqlite3
import json
import sys

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
        
def hash_password(password):
    return ""

def login_auth(username, password):
    hash = hash_password(password)
    with open("users.json", "r") as userFile:
        users = json.loads(userFile.read())
        if username in users:
            if hash == users[username]:
                return True
    return False

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
        session['token'] = "1234"
        valid_tokens.append(session['token'])
        print("received")
        return redirect("http://127.0.0.1:5173")
    return redirect("http://127.0.0.1:5173/login")


@app.route("/register", methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    session['username'] = username
    saveUser(username, hash_password(password))
    token = "1234"
    session['token'] = token
    print(session)
    valid_tokens.append(token)
    print("received")
    return redirect("http://127.0.0.1:5173")

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('token', None)
    return redirect("http://127.0.0.1:5173")

@app.route("/log", methods=["POST"])
def log():
    print(request.cookies)
    print(session)
    if (session_auth(session)):
        return "", 200
    # abort(403)
    return "", 403

@app.route("/getUserSleepData", methods=["GET"])
def getUserSleepData():
    with open("users.json","r") as userFile:
        for i in userFile:
            if session['username'] == i["username"]:
                dayNumber = i["sleepData"]["today"]
                if dayNumber == 1:
                    day = "monday"
                elif dayNumber == 2:
                    day = "tuesday"
                elif dayNumber == 3:
                    day = "wednesday"
                elif dayNumber == 4:
                    day = "thursday"
                elif dayNumber == 5:
                    day = "friday"
                elif dayNumber == 6:
                    day = "saturday"
                elif dayNumber == 7:
                    day = "sunday"
                dataToBeSent = dict(data = 0, weeksum = i["sleepData"]["weekSum"], username = i["username"])