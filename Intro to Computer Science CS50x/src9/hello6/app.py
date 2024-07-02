# Switches to POST

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# methods is a named argument
# post does not display in URL, good for privacy
# https://www.geeksforgeeks.org/flask-http-methods-handle-get-post-requests/ 
@app.route("/greet", methods=["POST"])
def greet():
    # instead of request.args
    return render_template("greet.html", name=request.form.get("name", "world"))
