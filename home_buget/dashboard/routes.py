from home_buget import db, bcrypt, app
from flask import Blueprint, flash, url_for, redirect, render_template


controller = Blueprint(
    "controller", template_folder="templates", static_url_path="static"
)


@controller("/controller_dashbd")
def secure_controller():
    return render_template("budget_planing.html")



