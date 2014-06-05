from app import db, photo
from hashlib import sha512
from uuid import uuid4

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(128), unique = True)
    hashed_password = db.Column(db.String(64))
    salt = db.Column(db.String(64))
    is_authenticated = False
    is_active = True

    def create(self, login, email, password):
        self.login = login
        self.salt = uuid4().hex
        self.hashed_password = sha512(password + self.salt).hexdigest()
        self.email = email

    def auth(self, login, password):
        u = User.query.filter(User.login == login).first()
        if u and sha512(password + u.salt).hexdigest() == u.hashed_password:
            self.id = u.id
            self.login = u.login
            self.email = u.email
            self.hashed_password = u.hashed_password
            self.salt = u.salt
            self.is_authenticated = True
            return True
        return False

    def is_authenticated(self):
        return self.is_authenticated

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %s>' % self.login

class Journey(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(128))
    description = db.Column(db.Text())

    def create(self, title, description, user_id):
        self.user_id = user_id
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Journey %s>' % self.title

class Slide(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    journey_id = db.Column(db.Integer, db.ForeignKey('journey.id'))
    title = db.Column(db.String(128))
    description = db.Column(db.Text())

    def create(self, title, description, journey_id):
        self.journey_id = journey_id
        self.title = title
        self.description = description

    def __repr__(self):
        return '<SlideShow %s>' % self.title

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    slide_id = db.Column(db.Integer, db.ForeignKey('slide.id'))
    title = db.Column(db.String(128))
    description = db.Column(db.Text())
    small = db.Column(db.String(128))
    medium = db.Column(db.String(128))
    large = db.Column(db.String(128))
    original = db.Column(db.String(128))

    def create(self, title, description, slide_id, path):
        self.slide_id = slide_id
        self.title = title
        self.description = description
        name = uuid4().hex
        self.original = photo.original(path, name)
        self.large = photo.large(path, name)
        self.medium = photo.medium(self.large, name)
        self.small = photo.small(self.medium, name)

    def __repr__(self):
        return '<Photo %s>' % self.title
