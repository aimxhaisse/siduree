from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, HiddenField, FileField, SelectField
from wtforms.validators import Required, EqualTo, Email

# User

class LoginForm(Form):
    login = TextField('Login', [Required()])
    password = PasswordField('Password', [Required()])

class RegisterForm(Form):
    login = TextField('Login', [Required()])
    email = TextField('Email', [Required(), Email()])
    password = PasswordField('Password', [Required(), EqualTo('again', message='Passwords must match')])
    again = PasswordField('Repeat Password')

# Journeys

class NewJourneyForm(Form):
    title = TextField('Title', [Required()])
    description = TextAreaField('Description')
    cover_id = SelectField('Cover', coerce=int)

class EditJourneyForm(Form):
    journey_id = HiddenField('Journey', [Required()])
    title = TextField('Title', [Required()])
    description = TextAreaField('Description')
    cover_id = SelectField('Cover', coerce=int)

class DeleteJourneyForm(Form):
    journey_id = HiddenField('Journey', [Required()])

# Slides

class NewSlideForm(Form):
    title = TextField('Title', [Required()])
    journey_id = HiddenField('Journey', [Required()])
    description = TextAreaField('Description')

class EditSlideForm(Form):
    slide_id = HiddenField('Slide', [Required()])
    title = TextField('Title', [Required()])
    description = TextAreaField('Description')
    cover_id = SelectField('Cover', coerce=int)

class DeleteSlideForm(Form):
    slide_id = HiddenField('Slide', [Required()])

# Photos

class NewPhotoForm(Form):
    title = TextField('Title', [Required()])
    photo = FileField('Your Photo', [Required()])
    slide_id = HiddenField('Slide', [Required()])
    description = TextAreaField('Description')

class EditPhotoForm(Form):
    photo_id = HiddenField('Photo', [Required()])
    title = TextField('Title', [Required()])
    description = TextAreaField('Description')

class DeletePhotoForm(Form):
    photo_id = HiddenField('Photo', [Required()])
