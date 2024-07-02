from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

## Configure session ##
app.config["SESSION_PERMANENT"] = False # delete on close
app.config["SESSION_TYPE"] = "filesystem" # store shopping cart on server, not cookie
Session(app)


@app.route("/")
def index():
    # books for sale
    books = db.execute("SELECT * FROM books")
    return render_template("books.html", books=books)


@app.route("/cart", methods=["GET", "POST"])
def cart():

    # Ensure cart exists
    if "cart" not in session:
        # initialize empty list as cart
        session["cart"] = []

    # POST
    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(book_id)
        # recursive call with "GET" instead of "POST" 
        return redirect("/cart")

    # GET
    # books in user's cart using cs50's (?) placeholder for list
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books=books)
