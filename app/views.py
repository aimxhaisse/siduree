from app import app, db
from flask import render_template, request, url_for, flash, redirect
from forms import LoginForm, RegisterForm
from misc import flash_errors
from models import User
from flask.ext.login import login_required, login_user, logout_user, current_user

@app.route('/')
def index():
    return render_template('index.html', title = 'Welcome!')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')
    form = LoginForm()
    if form.validate_on_submit():
        u = User()
        if u.auth(form.data['login'], form.data['password']):
            login_user(u)
            flash('Logged in successfully.', 'success')
            return redirect(request.args.get('next') or url_for('index'))
        flash('Login and password don\'t match', 'danger')
    flash_errors(form)
    return render_template('login.html', form = form, title = 'Sign In')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect('/')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            u = User(form.data['login'], form.data['password'], form.data['email'])
            db.session.add(u)
            db.session.commit()
            u.auth(form.data['login'], form.data['password'])
        except:
            flash('unable to create account, this login or email address is already in use', 'danger')
            return render_template('register.html', form = form, title = 'Register')
        return redirect('index')
    flash_errors(form)
    return render_template('register.html', form = form, title = 'Register')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html', form = RegisterForm(), title = 'About')
