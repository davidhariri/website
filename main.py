from flask import (
    Flask,
    render_template
)

app = Flask(__name__)


@app.route("/")
def render_home():
    posts = [
        {
            "text": {
                "html": "<p><b>Hello 👋</b> I'm currently working on a new version of my site. It's going to be <i>great</i> when it's finished. Until then, you can follow along <a href=\"https://github.com/davidhariri/website/\">on Github</a> or talk to me <a href=\"https://twitter.com/davehariri/\">on Twitter</a>. 🖖</p>",
                "md": "**Hello 👋** I'm currently working on a new version of my site. It's going to be *great* when it's finished. Until then, you can follow along [on Github](https://github.com/davidhariri/website) or talk to me [on Twitter](https://twitter.com/davehariri/). 🖖"
            },
            "media": [
                {
                    "type": "image/png",
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
                "friendly": "August 23 2017"
            }
        }
    ]

    return render_template("views/home.html", **locals())