import os
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_mongoengine import MongoEngine, MongoEngineSession, MongoEngineSessionInterface
from flask_user import login_required, UserManager, UserMixin, current_user, roles_required
from flask_login import logout_user
from flask_wtf.csrf import CSRFProtect, CSRFError
import datetime
from datetime import timedelta
import requests

from config import ConfigClass

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

if os.environ.get("FDT") == "ON":
    from flask_debugtoolbar import DebugToolbarExtension

# --- // Application Factory Setup (based on the Flask-User example for MongoDB)
# https://flask-user.readthedocs.io/en/latest/mongodb_app.html
# Setup Flask and load app.config
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(__name__ + ".ConfigClass")
csrf = CSRFProtect(app)
csrf.init_app(app)

if os.environ.get("FDT") == "ON":
    app.debug = True

# Setup Flask-MongoEngine --> MongoEngine --> PyMongo --> MongoDB
db = MongoEngine(app)

# Use Flask Sessions with Mongoengine
app.session_interface = MongoEngineSessionInterface(db)

# Initiate the Flask Debug Toolbar Extension
if os.environ.get("FDT") == "ON":
    toolbar = DebugToolbarExtension(app)


# --- // Classes -> MongoDB Collections: User.
# Flask-User User Class (Collection) extended with email_confirmed_at
# Added username indexing and background-indexing for performance
class User(db.Document, UserMixin):
    # Active set to True to allow login of user
    active = db.BooleanField(default=True)

    # User authentication information
    username = db.StringField(default="")
    password = db.StringField()

    # User information
    first_name = db.StringField(default="")
    last_name = db.StringField(default="")
    email = db.StringField(default="")
    email_confirmed_at = db.DateTimeField()
    # Required for the e-mail confirmation, and subsequent login.

    # Relationships  (Roles: user or user and Admin)
    roles = db.ListField(db.StringField(), default=["user"])

    meta = {
        "auto_create_index": True,
        "index_background": True,
        "indexes": ["username"]
    }


# Setup Flask-User and specify the User data-model
user_manager = UserManager(app, db, User)


# --- // Mind Timer Main Routes (Endpoints): CRUD.
@app.route("/")
@app.route("/index")
@app.route("/index.html")
def home_page():
    """
    Landing/Home Page, accessible before sign in/login. If logged in, user is redirected to the Mind Timer Page.
    At first access/touch the user 'admin' is created using environment variables for the password and email address.
    The user creation is here as it will be created twice on Heroku if placed in the main code.
    """
    if current_user.is_authenticated:
        return redirect(url_for("timer"))

    # Create admin user as first/default user, if admin does not exist.
    # Password and e-mail are set using environment variables.
    if not User.objects.filter(User.username == "admin"):
        try:
            user = User(
                username="admin",
                first_name="Administrator",
                last_name="Administrator",
                email=os.environ.get("MAIL_DEFAULT_SENDER"),
                email_confirmed_at=datetime.datetime.utcnow(),
                password=user_manager.hash_password(os.environ.get("ADMIN_PASSWORD"))
            )
            user.roles.append("Admin")
            user.save()

            flash("'admin' account created.", "success")
            app.logger.info("'admin' account is created at startup if the user doesn't exist: [SUCCESS] - (index.html).")
        except Exception:
            flash("'admin' account not created.", "danger")
            app.logger.critical("'admin' account is created at startup if the user doesn't exist: [FAILURE] - (index.html).")

    return render_template("index.html")

# Main MindTimer Application Page
@login_required
@app.route("/timer")
def timer():
    """
    The "R" in CRUD, authenticated user access to the MindTimer Application.
    """
    return render_template("timer.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blog_post")
def blog_post():
    return render_template("blog_post.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")


# --- // Error Handlers for 400 CSRF Error (Bad Request), 404 Page Not Found, 405 Method Not Allowed, and 500 Internal Server Error.
@app.errorhandler(CSRFError)
def handle_csrf_error(error):
    excuse = "Apologies, the Security Detail have omitted to secure this page! We're calling them back from their lunch-break to fix this. Please click on the pink pulsating buoy to go to the Home Page (registering or signing in) or Member's Page (signed in), or click on Sign Out below."
    return render_template("oops.html", error=error.description, excuse=excuse, error_type="Client: 400 - Bad Request")


@app.errorhandler(404)
def not_found_404(error):
    excuse = "Apologies, we're all lost and have no idea how this happened! Please click on the pink pulsating buoy to go to the Home Page (registering or signing in) or Member's Page (signed in), or click on Sign Out below."
    return render_template("oops.html", error=error, excuse=excuse, error_type="Client: 404 - Page Not Found")


@app.errorhandler(405)
def not_found_405(error):
    excuse = "Apologies, our we can't allow you to do this! Please click on the pink pulsating buoy to go to the Home Page (registering or signing in) or Member's Page (signed in), or click on Sign Out below."
    return render_template("oops.html", error=error, excuse=excuse, error_type="Client: 405 - Method Not Allowed")


@app.errorhandler(500)
def internal_error(error):
    excuse = "Apologies, something serious occurred and we're working on resolving the issue! This section is cordoned off for now. Please click on the pink pulsating buoy to go to the Home Page (registering or signing in) or Member's Page (signed in), or click on Sign Out below."
    return render_template("oops.html", error=error, excuse=excuse, error_type="Server: 500 - Internal Server Error")


# export PRODUCTION=ON | OFF in TEST
# PRODUCTION App -> Settings -> Reveal Config Vars -> KEY: PRODUCTION,
# VALUE: ON
if __name__ == "__main__":
    if not os.environ.get("MONGO_URI"):
        raise ValueError(
            "MongoDB Uniform Resource Identifier is missing, which means that we can't access the database.")
    elif not os.environ.get("ADMIN_PASSWORD"):
        raise ValueError(
            "Admin Password is not set which means that the Admin user can not be created.")
    elif not os.environ.get("MAIL_SERVER"):
        raise ValueError(
            "Mail Server Configuration error: MAIL_SERVER is not defined.")
    elif not os.environ.get("MAIL_PORT"):
        raise ValueError(
            "Mail Server Configuration error: MAIL_PORT is not defined.")
    elif not os.environ.get("MAIL_USERNAME"):
        raise ValueError(
            "Mail Server Configuration error: MAIL_USERNAME is not defined.")
    elif not os.environ.get("MAIL_PASSWORD"):
        raise ValueError(
            "Mail Server Configuration error: MAIL_PASSWORD is not defined.")
    elif not os.environ.get("USER_EMAIL_SENDER_EMAIL"):
        raise ValueError(
            "Mail Server Configuration error: USER_EMAIL_SENDER_EMAIL is not defined.")
    elif os.environ.get("APPDEBUG") == "ON":
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=True)
    else:
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=False)