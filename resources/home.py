from flask import render_template
from flask_smorest import Blueprint


blp = Blueprint("Home", __name__, description="Operation on index page.")

# homepage 
@blp.route("/")
@blp.route("/home")
def home():
    return render_template('index.html')