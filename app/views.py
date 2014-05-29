from app import app
from flask import render_template, request, url_for, flash
from forms import LoginForm, RegisterForm
from misc import flash_errors

@app.route('/')
def index():
    return render_template('index.html', title = 'Welcome!')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.auth(form.login, form.password)
        if u:
            login_user(u)
            flash('Logged in successfully.')
            return redirect(url_for('index'))
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
