# Adds a form, second route

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # index.html is seen on initial website visit
    return render_template("index.html")


@app.route("/greet")
def greet():
    # greet.html is seen when submit is clicked
    name = request.args.get("name", "world")
    # correct for empty string
    if name == "":
        name = "world"
    return render_template("greet.html", name=name)
# alternatively hello8/templates/greet.html has Jinja solution

"""
@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))
"""
