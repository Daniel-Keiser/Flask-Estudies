from flask import render_template
from AppFlask import app

@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):

    return render_template('index.html', user = user)

@app.route("/login")
def login(user):
    return render_template('base.html', user = user)