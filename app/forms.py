from flask_wtf import Form
from wtforms import TextField, IntegerField, DecimalField
from wtforms.validators import DataRequired

class userForm(Form):
    username = TextField('username', validators=[DataRequired()])

class tripForm(Form):
    destination = TextField('destination', validators=[DataRequired()])

class expenseForm(Form):
    username = TextField('username', validators=[DataRequired()])
    trip_id = TextField('trip_id', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    value = TextField('value', validators=[DataRequired()])
