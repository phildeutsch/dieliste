from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    expenses = db.relationship('Expenses', backref='user', lazy='dynamic')
    trips = db.relationship('Trips', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Trips(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        s = '<Trip {0}>'
        return  s.format(self.id)


class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))
    description = db.Column(db.String(140))
    value = db.Column(db.Float)

    def __repr__(self):
        s = '<Expense {0}: {1}>'
        return  s.format(self.description, self.value)
