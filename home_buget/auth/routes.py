from home_buget import db, app, bcrypt
from flask import render_template, redirect, url_for, flash, Blueprint


authent = Blueprint("authent", template_folder="templates", static_url_path="static")


@authent.route("/register")
def secure_register():
    return render_template("signup.html")



@authent.route("/login")
def secure_login():
    return render_template("login.html")