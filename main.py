from flask import (
    Flask,
    render_template
)
import os
import requests

app = Flask(__name__)


@app.route("/")
def render_home():
    response = requests.get("https://dhariri-api.herokuapp.com/notes/nWsMjv3/").json()

    return render_template("views/home.html", posts=[response])
