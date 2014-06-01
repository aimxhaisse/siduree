from app import app, db, login_manager
from flask.ext.login import login_url
from flask import render_template, request, url_for, flash, redirect
from forms import LoginForm, RegisterForm, NewJourneyForm, NewSlideForm
from misc import flash_errors
from models import User, Journey, Slide
from flask.ext.login import login_required, login_user, logout_user, current_user

# Main pages
@app.route('/')
def index():
    return render_template('index.html', title = 'Welcome!')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html', title = 'About')

# Journeys
@app.route('/new-journey', methods = ['GET', 'POST'])
@login_required
def new_journey():
    form = NewJourneyForm()
    if form.validate_on_submit():
        j = Journey()
        j.create(form.data['title'], form.data['description'], current_user.id)
        db.session.add(j)
        db.session.commit()
        flash('Journey %s successfully created.' % j.title, 'success')
        return redirect(url_for('new_slide', jid = j.id))
    flash_errors(form)
    return render_template('new-journey.html', form = form, title = 'New Journey')

# Slides
@app.route('/new-slide', methods = ['GET', 'POST'])
@login_required
def new_slide():
    jid = request.args.get('jid') or None
    form = NewSlideForm(journey_id = jid)
    if form.validate_on_submit():

        # make sure the journey is owned by the user
        is_this_illegal = False
        if jid:
            j = Journey.query.filter_by(id = jid).first()
            if not j or j.user_id != current_user.id:
                is_this_illegal = True
        else:
            is_this_illegal = True
        if is_this_illegal:
            flash('Hey! Don\'t try that again!', 'danger')
            return redirect(url_for('index'))

        s = Slide()
        s.create(form.data['title'], form.data['description'], form.data['journey_id'])
        db.session.add(s)
        db.session.commit()
        flash('Slide added to journey', 'success')
        return redirect(url_for('index'))
    flash_errors(form)
    return render_template('new-slide.html', form = form, title = 'New Slide')

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
