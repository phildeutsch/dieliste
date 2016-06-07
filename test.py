from app import models, db

models.User.query.delete()
models.Trip.query.delete()
models.Expense.query.delete()

u1 = models.User(username='tom', email='tom@test.com')
u2 = models.User(username='jerry', email='jerry@test.com')
db.session.add(u1)
db.session.add(u2)

t = models.Trip(destination="some destination")
t.users.append(u1)
t.users.append(u2)
db.session.add(t)

db.session.add(models.Expense(user_id=1, trip_id=1, description='Beer', value=17))


db.session.commit()

print(models.User.query.all())
print(models.Trip.query.all())
print(models.Expense.query.all())

tom = models.User.query.get(1)
