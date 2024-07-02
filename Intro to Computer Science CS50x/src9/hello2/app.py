# Uses parameter with same name as variable

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    if "name_query" in request.args:
        name_app = request.args["name_query"]
    # else:
    #     name_app = "world"
    return render_template("index.html", name_html=name_app)

# flask run
# http://127.0.0.1:5000/?name_query=ddangman
## will break w/o /?name=ddangman
## uncomment lines 12-13 to work