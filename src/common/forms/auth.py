from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField(
        "Correo",
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Contraseña",
        validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField("Entrar")


class SignUpForm(FlaskForm):
    username = StringField(
        "Usuario",
        validators=[DataRequired(), Length(min=3)]
    )
    email = StringField(
        "Correo",
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        "Contraseña",
        validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField("Entrar")