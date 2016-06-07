from flask_wtf import Form
from wtforms import TextField, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired

class userForm(Form):
    username = TextField('username', validators=[DataRequired()])

class tripForm(Form):
    destination = TextField('destination', validators=[DataRequired()])

class expenseForm(Form):
    #trip_id = SelectField('trip_id', validators=[DataRequired()],
    #    choices = [(1,'One'), (2, 'Two')])

    trip_id = IntegerField('trip_id', validators=[DataRequired()])
    user_id = IntegerField('user_id', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    value = TextField('value', validators=[DataRequired()])
