from app import app
from flask import render_template
from forms import LoginForm
from forms import RegisterForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Welcome!')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html', form = LoginForm(), title = 'Sign In')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register.html', form = RegisterForm(), title = 'Register')
