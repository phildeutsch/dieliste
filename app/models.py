from app import db

association_table  = db.Table('association',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('trip_id', db.Integer, db.ForeignKey('trip.id')),
    db.Column('expense_id', db.Integer, db.ForeignKey('expense.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    expenses = db.relationship('Expense', backref='user')
    trips = db.relationship('Trip', secondary=association_table, back_populates='users')

    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        s = '<User {0}: {1}>'
        return s.format(self.id, self.username)

class Trip(db.Model):
    __tablename__ = 'trip'
    id = db.Column(db.Integer, primary_key=True)

    expenses = db.relationship('Expense', backref='trip')
    users = db.relationship('User', secondary=association_table, back_populates='trips')

    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    destination = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        s = '<Trip {0} to {1}>'
        return  s.format(self.id, self.destination)

class Expense(db.Model):
    __tablename__ = 'expense'
    id = db.Column(db.Integer, primary_key = True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'))

    timestamp = db.Column(db.DateTime)
    description = db.Column(db.String(140))
    value = db.Column(db.Float)

    def __repr__(self):
        s = '<Expense {0}: {1} paid {2} on trip {3} for {4}>'
        return  s.format(self.id, self.user_id, self.value, self.trip_id, self.description)
