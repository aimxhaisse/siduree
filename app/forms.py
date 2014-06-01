from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, HiddenField
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

class DeleteJourneyForm(Form):
    journey_id = HiddenField('Journey', [Required()])

class EditJourneyForm(Form):
    journey_id = HiddenField('Journey', [Required()])
    title = TextField('Title', [Required()])
    description = TextAreaField('Description')

# Slides

class NewSlideForm(Form):
    title = TextField('Title', [Required()])
    journey_id = HiddenField('Journey', [Required()])
    description = TextAreaField('Description')

class DeleteSlideForm(Form):
    slide_id = HiddenField('Slide', [Required()])
