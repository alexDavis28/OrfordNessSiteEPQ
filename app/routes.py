from app import app
from flask import render_template


# Home page
@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")
