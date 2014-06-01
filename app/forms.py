from flask.ext.wtf import Form
from wtforms import TextField
from wtforms import PasswordField
from wtforms.validators import Required
from wtforms.validators import EqualTo
from wtforms.validators import Email

class LoginForm(Form):
    login = TextField('Login', [Required()])
    password = PasswordField('Password', [Required()])

class RegisterForm(Form):
    login = TextField('Login', [Required()])
    email = TextField('Email', [Required(), Email()])
    password = PasswordField('Password', [Required(), EqualTo('again', message='Passwords must match')])
    again = PasswordField('Repeat Password')
