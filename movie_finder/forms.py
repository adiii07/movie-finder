from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    name = StringField("Movie Name", validators=[DataRequired()])
    submit = SubmitField("Search")