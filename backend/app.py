from flask import Flask

app = Flask(__name__)

@app.route("/log")
def log_sleep():
    return "<p>Hello, World!</p>"