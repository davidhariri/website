from flask import (
    Flask,
    render_template,
    abort
)
import requests

app = Flask(__name__)

API_ROOT = "https://dhariri-api.herokuapp.com"


@app.route("/")
def render_home():
    # FIXME: Temporary while I dial in the features
    response = requests.get("{}/notes/nWsMjv3/".format(API_ROOT)).json()

    return render_template("views/home.html", notes=[response])


@app.route("/notes/<note_id>/")
def render_note(note_id):
    note_resp = requests.get(
        "{}/notes/{}/".format(API_ROOT, note_id)
    )

    if note_resp.status_code != 200:
        abort(404)

    return render_template("views/note.html", note=note_resp.json())
