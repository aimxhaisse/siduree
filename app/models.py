from app import db
from hashlib import sha512
from uuid import uuid4

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(128), unique = True)
    hashed_password = db.Column(db.String(64))
    salt = db.Column(db.String(64))

    @staticmethod
    def auth(login, password):
        u = User.query.filter(User.login == login).first()
        if u and sha512(password + u.salt).hexdigest() == u.hashed_password:
            return u
        return None

    @staticmethod
    def new(login, password, email):
        u = User()
        u.login = login
        u.salt = uuid4().hex
        u.hashed_password = sha512(password + u.salt).hexdigest()
        u.email = email
        db.session.add(u)
        db.session.commit()
        return u

    def __repr__(self):
        return '<User %s>' % self.login

class Story(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(128))
    description = db.Column(db.Text())

    def __repr__(self):
        return '<Story %s>' % self.title
