from app import app, db, login_manager
from flask.ext.login import login_url
from flask import render_template, request, url_for, flash, redirect
from forms import LoginForm, RegisterForm
from misc import flash_errors
from models import User
from flask.ext.login import login_required, login_user, logout_user, current_user

# Main pages

@app.route('/')
def index():
    return render_template('index.html', title = 'Welcome!')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html', form = RegisterForm(), title = 'About')

# User management

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
    flash('Logged out successfully.', 'success')
    return redirect('/')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')
    form = RegisterForm()
    if form.validate_on_submit():
        u = User()
        u.create(form.data['login'], form.data['email'], form.data['password'])
        db.session.add(u)
        db.session.commit()
        login_user(u)
        flash('Account successfully created.', 'success')
        return redirect(url_for('index'))
    flash_errors(form)
    return render_template('register.html', form = form, title = 'Register')

@app.route('/me', methods = ['GET', 'POST'])
@login_required
def me():
    return render_template('me.html', title = 'My Account')

@login_manager.unauthorized_handler
def unauthorized():
    flash('You need to sign in to access this page', 'danger')
    return redirect(login_url(url_for('login'), request.url))
