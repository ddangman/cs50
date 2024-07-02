# Uses request.args.get

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # default request.args.get() return is None
    # name = request.args.get("name", None)
    # has dictionary behavior request.args.get("key", value)
    name = request.args.get("name", "world")
    return render_template("index.html", name=name)
