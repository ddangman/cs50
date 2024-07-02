# Uses a single route

from flask import Flask, render_template, request

app = Flask(__name__)


# handle both methods
@app.route("/", methods=["GET", "POST"]) # order doesn't matter
def index():
    if request.method == "POST":
        # Flask request object is POST
        return render_template("greet.html", name=request.form.get("name", "world"))
    # Flask request object must be GET
    return render_template("index.html")
