from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    Expenses = db.relationship('Expenses', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.String(140))
    value = db.Column(db.Float)

    def __repr__(self):
        return '<Post %r>' % (self.body)
