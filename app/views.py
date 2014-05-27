from app import app
from flask import render_template, request, url_for
from forms import LoginForm, RegisterForm

@app.route('/')
def index():
    return render_template('index.html', title = 'Welcome!')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html', form = LoginForm(), title = 'Sign In')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register.html', form = RegisterForm(), title = 'Register')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html', form = RegisterForm(), title = 'About')
