from flask import render_template, flash, redirect, url_for
from app import app, db
from .forms import userForm, tripForm, expenseForm
from .models import User, Trip, Expense

# index view function suppressed for brevity

@app.route('/index', methods=['GET', 'POST'])
def index():
    user_form = userForm()
    trip_form = tripForm()
    expense_form = expenseForm()

    if user_form.validate_on_submit():
        user = User()
        user_form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    if trip_form.validate_on_submit():
        trip = Trip()
        trip_form.populate_obj(trip)
        db.session.add(trip)
        db.session.commit()
        return redirect(url_for('index'))

    if expense_form.validate_on_submit():
        expense = Expense()
        expense_form.populate_obj(expense)
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("index.html",
                           title='Home',
                           users=User.query.all(),
                           trips=Trip.query.all(),
                           expenses=Expense.query.all(),
                           user_form=user_form,
                           trip_form=trip_form,
                           expense_form=expense_form)
