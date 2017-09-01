from flask import (
    Flask,
    render_template,
    abort
)
import requests

from ago import human
from datetime import datetime

app = Flask(__name__)

API_ROOT = "https://dhariri-api.herokuapp.com"


@app.template_filter("ago")
def render_date_ago(timestamp):
    d = datetime.fromtimestamp(timestamp)
    return human(d, 1)


@app.route("/")
@app.route("/notes/")
def render_home():
    # FIXME: Temporary while I dial in the features
    notes_resp = requests.get("{}/notes/".format(API_ROOT))

    return render_template("views/home.html", notes=notes_resp.json()["notes"])


@app.route("/notes/<note_id>/")
def render_note(note_id):
    note_resp = requests.get(
        "{}/notes/{}/".format(API_ROOT, note_id)
    )

    if note_resp.status_code != 200:
        abort(404)

    return render_template("views/note.html", note=note_resp.json())
