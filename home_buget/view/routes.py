from home_buget import app
from flask import redirect, Blueprint, render_template, url_for, flash


homepage = Blueprint("homepage", template_folder="templates", static_url_path="static")


@homepage.route("/homepage")
def homepage():
    return render_template("home.html")



