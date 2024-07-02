# session is essentially an empty dictionary that is persistant
# used as a replacement for the temporary global dict REGISTRANTS={}

from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

## Configure session ##
app.config["SESSION_PERMANENT"] = False # delete on close
app.config["SESSION_TYPE"] = "filesystem" # store shopping cart on server, not cookie
Session(app)


@app.route("/")
def index():
    return render_template("index.html", name=session.get("name"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # get unique shopping cart
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    # clear session server side
    session.clear()
    return redirect("/")
