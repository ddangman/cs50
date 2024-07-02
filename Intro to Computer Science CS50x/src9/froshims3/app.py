# Implements a registration form using checkboxes

from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    if not request.form.get("name"):
        return render_template("failure.html")
    # radio buttons are mutually exclusive
    # check boxes are inclusive [0,n]
    for sport in request.form.getlist("sport"):
        if sport not in SPORTS:
            return render_template("failure.html")

    # Confirm registration. render confirmation
    return render_template("success.html")
