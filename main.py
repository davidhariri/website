from flask import (
    Flask,
    render_template
)
import os

app = Flask(__name__)


@app.route("/")
def render_home():
    posts = [
        {
            "id": 1,
            "text": {
                "html": "<p>I'm currently working on a new version of my site. Follow along <a href=\"https://github.com/davidhariri/website/\">on Github</a> or talk to me <a href=\"https://twitter.com/davehariri/\">on Twitter</a>.</p>",
                "md": "I'm currently working on a new version of my site. Follow along [on Github](https://github.com/davidhariri/website) or talk to me [on Twitter](https://twitter.com/davehariri/)."
            },
            "media": [
                {
                    "type": "image/png",
                    "kind": "image",
                    "url": "https://ada.imgix.net/images/57487a7c-ba75-4ebf-abe8-fe5c14ee9f06.png",
                    "size": [1536, 2048]
                }
            ],
            "location": {
                "coordinates": [43.64920, -79.39720],
                "friendly": "Toronto",
            },
            "created": {
                "utc": "2017-08-23T19:35:43.511Z",
                "friendly": "August 23rd 2017"
            }
        }
    ]

    return render_template("views/home.html", **locals())


@app.route("/.well-known/acme-challenge/5wvUisl4hWbXhaQ1RvAQDI7hBBJicIlR13pc4MxeQFE")
def return_secret():
    return os.getenv("LE_CHALLENGE", "Bonk")
