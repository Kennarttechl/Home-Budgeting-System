from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length, EqualTo


class RegistterForm(FlaskForm):
    username = StringField(
        validators=[DataRequired(), Length(min=1, max=15)],
        render_kw={"placeholder": "Enter username"},
    )
    password = PasswordField(
        validators=[DataRequired(), Length(min=1, max=15)],
        render_kw={"placeholder": "Enter your password"},
    )
    confirm_password = PasswordField(
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"placeholder": "Confirm_Password"},
    )
