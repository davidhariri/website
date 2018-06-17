import os
import contentful
import markdown
from flask import Flask, render_template, redirect

app = Flask(__name__)
content = contentful.Client(
    os.getenv("CMS_ID"), os.getenv("CMS_KEY"))


@app.route("/")
def page_home():
    page = content.entry("25FCnRQOVGwge0kcSsSm2e")
    return render_template("home.html", **locals())


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/", code=302)
