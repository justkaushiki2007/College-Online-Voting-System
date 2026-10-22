from flask import Flask, render_template
from config import Config
from database.db import db

from models.user import User
from models.candidate import Candidate
from models.vote import Vote
from models.admin import Admin
from models.election import Election

from routes.auth import auth
from routes.candidate import candidate
from routes.vote import vote
from routes.admin import admin


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(candidate)
app.register_blueprint(vote)
app.register_blueprint(admin)


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/signup")
def signup_page():
    return render_template("signup.html")


@app.route("/vote")
def vote_page():
    return render_template("vote.html")


@app.route("/admin")
def admin_page():
    return render_template("admin.html")
@app.route("/thankyou")
def thankyou_page():
    return render_template("thankyou.html")
@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("dashboard.html")
with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)
