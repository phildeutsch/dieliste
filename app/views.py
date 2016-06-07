from flask import render_template, flash, redirect
from app import app
from .forms import userForm, tripForm, expenseForm
from .models import User, Trip, Expense

# index view function suppressed for brevity

@app.route('/index', methods=['GET', 'POST'])
def index():
    user_form = userForm()
    trip_form = tripForm()
    expense_form = expenseForm()

    return render_template("index.html",
                           title='Home',
                           users=User.query.all(),
                           trips=Trip.query.all(),
                           expenses=Expense.query.all(),
                           user_form=user_form,
                           trip_form=trip_form,
                           expense_form=expense_form)
