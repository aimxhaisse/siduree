from app import app
from flask import render_template, request, url_for, flash, redirect
from forms import LoginForm, RegisterForm
from misc import flash_errors
from models import User

@app.route('/')
def index():
    return render_template('index.html', title = 'Welcome!')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.auth(form.data['login'], form.data['password'])
        if u:
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))
        flash('Login and password don\'t match', 'danger')
    flash_errors(form)
    return render_template('login.html', form = form, title = 'Sign In')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('index')
    flash_errors(form)
    return render_template('register.html', form = form, title = 'Register')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html', form = RegisterForm(), title = 'About')
