from flask_wtf  import Form
from wtforms import TextField, IntegerField, DecimalField
from wtforms.validators import DataRequired

class expenseForm(Form):
    user_name = TextField('user_name', validators=[DataRequired()])
    trip_id = IntegerField('trip_id', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    value = DecimalField('value', validators=[DataRequired()])
