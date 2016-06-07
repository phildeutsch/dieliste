from flask import render_template, flash, redirect
from app import app
from .forms import expenseForm
from .models import User, Trip, Expense

# index view function suppressed for brevity

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = expenseForm()

    return render_template("index.html",
                           title='Home',
                           expenses=Expense.query.all(),
                           form=form)
