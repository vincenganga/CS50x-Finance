import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
# if not os.environ.get("API_KEY"):
    # raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    # Get the user info
    items = db.execute("SELECT symbol, name, price, SUM(shares) AS shares FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)

    # Cash that the user has
    cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash_db[0]["cash"]

    total = cash

    for item in items:
        total += item["price"] * item["shares"]

    return render_template("index.html", items=items, cash=cash, usd=usd, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # User reached out via POST
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        item = lookup(symbol)

        # Ensure symbol is submitted
        if not symbol:
            return apology("Enter a symbol")
        elif not item:
            return apology("Invalid symbol")

        # Ensure shares are integers
        try:
            shares = int(request.form.get("shares"))
        except:
            return apology("Shares must be an integer")

        # Ensure integer is positive
        if shares <= 0:
            return apology("Shares must be positive integers")

        # Obtain users information
        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        item_name = item["name"]
        item_price = item["price"]
        total_price = item_price * shares

        # Ensure user has enough cash to buy a share
        if cash < total_price:
            return apology("Not enough cash")

        # Update the users infomation if there is enough cash to buy
        else:
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total_price, user_id)
            db.execute("INSERT INTO transactions (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)", user_id, item_name, shares, item_price, "buy", symbol)

        flash("BOUGHT!")

        # Redirect user to home page
        return redirect("/")

    # User reached out via GET
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions_db = db.execute("SELECT symbol, price, shares, time FROM transactions WHERE user_id = ?", user_id)
    return render_template("history.html", transactions=transactions_db, usd=usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# Personal touch (adding cash)
@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """User can add cash"""
    # User reached out via GET
    if request.method == "GET":
        return render_template("add.html")

    # User reached out via POST
    else:
        added_cash = int(request.form.get("added_cash"))

        # Ensure the placeholder is not empty
        if not added_cash:
            return apology("Enter amount of money to be added")

        # Update the user table with more cash
        user_id = session["user_id"]
        cash_db = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        user_cash = cash_db[0]["cash"]

        uptd_cash = user_cash + added_cash

        # UPDATE table_name SET column1 = value1, column2 = value2, ...WHERE condition;
        db.execute("UPDATE users SET cash = ? WHERE id = ?", uptd_cash, user_id)

        # Redirect user to the main page
        return redirect("/")


# Personal touch (changing password)
@app.route("/newpassword", methods=["GET", "POST"])
@login_required
def new_password():
    """Allow user to change password"""
    # User reached out via GET
    if request.method == "GET":
        return render_template("newpassword.html")

    # User reached out via POST
    else:
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirm_new_password = request.form.get("confirm_new_password")

        # Ensure the placeholder is not empty
        if not current_password:
            return apology("Input the current password", 403)

        # Ensure current password is correct
        old_password = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])

        if len(old_password) != 1 or not check_password_hash(old_password[0]["hash"], current_password):
            return apology("Invalid username and/or password")

        # Ensure new password was submitted
        if not new_password:
            return apology("Input new password")

        # Ensure confirmation of password was submitted
        elif not confirm_new_password:
            return apology("Confirm your new password")

        # Ensure both passwords match
        elif new_password != confirm_new_password:
            return apology("Passwords do not match")

        # Update the new password to the database
        hashed_new_password = generate_password_hash(new_password)

        db.execute("UPDATE users SET hash = ? WHERE id = ?", hashed_new_password, session["user_id"])

        # Redirect the user to login form
        return redirect("/logout")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User reached out via POST
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Ensure quote is submitted
        if not symbol:
            return apology("Please enter a symbol")

        item = lookup(symbol)

        # Ensure the item is valid
        if not item:
            return apology("Please enter a valid symbol")

        return render_template("quoted.html", item=item, usd=usd)

    # User reached out via GET
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached out via GET
    if request.method == "GET":
        return render_template("register.html")

    # User reached out via POST
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure that the username, password and confirmation password are submitted
        if not username:
            return apology("Must provide a username")

        if not password:
            return apology("Must provide a password")

        if not confirmation:
            return apology("Must provide confirmation password")

        # Ensure password and confirmation password are the same
        if password != confirmation:
            return apology("Password and confirmation password do not match")

        # Make the users password secure with hash
        hash = generate_password_hash(password)

        try:
            # INSERT INTO table_name (column1, column2,) VALUES (value1, value2)
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("Username already exists")

        # Redirect the user to the index page
        session["user_id"] = new_user

        # Redirect user to homepage
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # User reached out via POST
    if request.method == "POST":
        user_id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        # Ensure shares are positive numbers
        if shares <= 0:
            return apology("Shares must be a positive number")

        # Check price and name of stock
        item_price = lookup(symbol)["price"]
        item_name = lookup(symbol)["name"]
        price = shares * item_price

        # Ensure user has the correct amount of shares that can be sold
        shares_owned = db.execute("SELECT shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol", user_id, symbol)[0]["shares"]

        if shares_owned < shares:
            return apology("You don't have that many shares")

        # Update the database if the transaction is successful
        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        db.execute("UPDATE users SET cash = ? WHERE id = ?", current_cash + price, user_id)
        db.execute("INSERT INTO transactions (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)", user_id, item_name, -shares, item_price, "sell", symbol)

        flash("SOLD!")

        # Redirect user to home page
        return redirect("/")

    # User reached out via GET
    else:
        user_id = session["user_id"]

        symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
        return render_template("sell.html", symbols=symbols)
