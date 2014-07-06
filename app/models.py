from app import db, photo
from hashlib import sha512
from uuid import uuid4
import os

UPLOAD_RESOURCE = 'uploads/'
IMAGE_NOT_FOUND = 'notfound-800.png'

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(64), unique = True)
    email = db.Column(db.String(128), unique = True)
    hashed_password = db.Column(db.String(64))
    salt = db.Column(db.String(64))
    is_authenticated = False
    is_active = True
    journeys = db.relationship('Journey', backref='user', lazy='dynamic')

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
    cover_id = db.Column(db.Integer, db.ForeignKey('slide.id', use_alter = True, name = 'journey_cover'), nullable = True)

    def create(self, title, description, user_id):
        self.user_id = user_id
        self.title = title
        self.description = description

    def __repr__(self):
        return '<Journey %s>' % self.title

    def get_cover(self):
        try:
            s = Slide.query.filter_by(id = self.cover_id).first()
            return s.get_cover()
        except:
            return 'img/%s' % IMAGE_NOT_FOUND

class Slide(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    journey_id = db.Column(db.Integer, db.ForeignKey('journey.id'))
    journey = db.relationship('Journey', backref = db.backref('slides', lazy = 'dynamic'), foreign_keys = 'Slide.journey_id')
    title = db.Column(db.String(128))
    description = db.Column(db.Text())
    cover_id = db.Column(db.Integer, db.ForeignKey('photo.id', use_alter = True, name = 'slide_cover'), nullable = True)

    def create(self, title, description, journey_id):
        self.journey_id = journey_id
        self.title = title
        self.description = description

    def get_cover(self):
        try:
            cover = Photo.query.filter_by(id = self.cover_id).first()
            if not cover:
                cover = Photo.query.filter_by(slide_id = self.id).first()
            return '%s/%s' % (UPLOAD_RESOURCE, cover.medium)
        except:
            return 'img/%s' % IMAGE_NOT_FOUND

    def __repr__(self):
        return '<SlideShow %s>' % self.title

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    slide_id = db.Column(db.Integer, db.ForeignKey('slide.id'))
    slide = db.relationship('Slide', backref = db.backref('photos', lazy = 'dynamic'), foreign_keys = 'Photo.slide_id')
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

        orig_fp = photo.original(path, name)
        large_fp = photo.large(orig_fp, name)
        medium_fp = photo.medium(large_fp, name)
        small_fp = photo.small(medium_fp, name)

        self.original = os.path.basename(orig_fp)
        self.large = os.path.basename(large_fp)
        self.medium = os.path.basename(medium_fp)
        self.small = os.path.basename(small_fp)

    def get_large(self):
        return '%s/%s' % (UPLOAD_RESOURCE, self.large)

    def get_medium(self):
        return '%s/%s' % (UPLOAD_RESOURCE, self.medium)

    def __repr__(self):
        return '<Photo %s>' % self.title
