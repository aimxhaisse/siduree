from flask.ext.wtf import Form
from wtforms import TextField
from wtforms import PasswordField
from wtforms.validators import Required
from wtforms.validators import EqualTo

class LoginForm(Form):
    login = TextField('Login', [Required()])
    password = PasswordField('Password', [Required()])

class RegisterForm(Form):
    login = TextField('Login', [Required()])
    password = PasswordField('Password', [Required(), EqualTo('again', message='Passwords must match')])
    again = PasswordField('Repeat Password')
