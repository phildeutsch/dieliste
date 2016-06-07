from flask_wtf import Form
from wtforms import TextField, IntegerField, DecimalField
from wtforms.validators import DataRequired

class userForm(Form):
    user_name = TextField('user_name', validators=[DataRequired()])

class tripForm(Form):
    destination = TextField('destination', validators=[DataRequired()])

class expenseForm(Form):
    user_name = TextField('user_name', validators=[DataRequired()])
    trip_id = TextField('trip_id', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    value = TextField('value', validators=[DataRequired()])
