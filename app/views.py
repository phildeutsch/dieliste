from flask import render_template, flash, redirect
from app import app
from .forms import expenseForm

# index view function suppressed for brevity

@app.route('/index')
def index():
    expenses = [
        {
            'user' : {'nickname': 'Tom'},
            'trip' : 2,
            'description' : 'Beer',
            'value' : 17
        },
        {
            'user' : {'nickname': 'Jerry'},
            'trip' : 2,
            'description' : 'Pizza',
            'value' : 12
        }
    ]

    return render_template("index.html",
                           title='Home',
                           expenses=expenses)
