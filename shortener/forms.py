from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ShortenForm(FlaskForm):
    originalUrl = StringField('Original Url', validators=[DataRequired()], render_kw={"placeholder": "Exemple: https://github.com/octafox/"})
    submit = SubmitField('Shorten')