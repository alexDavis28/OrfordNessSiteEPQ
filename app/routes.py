from app import app
from flask import render_template


# Home page
@app.route('/')
@app.route("/index")
def hello_world():
    return render_template("index.html")
