import os
import contentful
from flaskext.markdown import Markdown
from flask import Flask, render_template, redirect

app = Flask(__name__)
Markdown(app)


content = contentful.Client(
    os.getenv("CMS_ID"), os.getenv("CMS_KEY"))


@app.route("/")
def page_home():
    page = content.entry("25FCnRQOVGwge0kcSsSm2e")
    return render_template("page.html", **locals())


@app.route("/tests/<template>")
def page_ada_tests(template):
    return render_template("tests/" + template)


@app.errorhandler(404)
def page_not_found(e):
    return redirect("/", code=302)
