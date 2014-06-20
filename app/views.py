from app import app, db, login_manager
from flask.ext.login import login_url
from flask import render_template, request, url_for, flash, redirect
from forms import LoginForm, RegisterForm
from forms import NewJourneyForm, EditJourneyForm, DeleteJourneyForm
from forms import NewSlideForm, EditSlideForm, DeleteSlideForm
from forms import NewPhotoForm, EditPhotoForm, DeletePhotoForm
from misc import flash_errors
from models import User, Journey, Slide, Photo
from flask.ext.login import login_required, login_user, logout_user, current_user
import tempfile

BAD_KITTY = 'Hey! Don\'t try that again!'

# --- MAIN PAGES

@app.route('/')
def index():
    return render_template('index.html', title = 'Welcome!')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html', title = 'About')

# --- JOURNEYS

@app.route('/view-journey/<int:journey_id>')
def view_journey(journey_id):
    journey = Journey.query.filter_by(id = journey_id, user_id = current_user.id).first()
    if not journey:
        flash('This journey does not exist anymore.', 'danger')
        return redirect(url_for('index'))
    return render_template('view-journey.html', journey = journey)

@app.route('/new-journey', methods = ['GET', 'POST'])
@login_required
def new_journey():
    form = NewJourneyForm()

    if form.validate_on_submit():
        journey = Journey()
        journey.create(form.data['title'], form.data['description'], current_user.id)
        db.session.add(journey)
        db.session.commit()
        flash('Journey %s successfully created.' % journey.title, 'success')
        return redirect(url_for('new_slide', journey_id = journey.id))

    flash_errors(form)
    return render_template('new-journey.html', form = form, title = 'New Journey')

@app.route('/delete-journey/<int:journey_id>', methods = ['GET', 'POST'])
@login_required
def delete_journey(journey_id):
    journey = Journey.query.filter_by(id = journey_id, user_id = current_user.id).first()
    if not journey:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))

    form = DeleteJourneyForm(journey_id = journey_id)

    if form.validate_on_submit():
        Journey.query.filter(Journey.id == journey_id).delete()
        db.session.commit()
        flash('Journey successfully deleted.', 'success')
        return redirect(url_for('me'))

    flash_errors(form)
    return render_template('delete-journey.html', form = form, journey = journey, title = 'Delete journey %s' % journey.title)

@app.route('/edit-journey/<int:journey_id>', methods = ['GET', 'POST'])
@login_required
def edit_journey(journey_id):
    journey = Journey.query.filter_by(id = journey_id, user_id = current_user.id).first()

    if not journey:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))

    form = EditJourneyForm(journey_id = journey_id, title = journey.title, description = journey.description)

    if form.validate_on_submit():
        journey.title = form.data['title']
        journey.description = form.data['description']
        db.session.commit()
        flash('Journey successfully updated.', 'success')
        return redirect(url_for('me'))

    slides = Slide.query.filter_by(journey_id = journey_id)

    flash_errors(form)
    return render_template('edit-journey.html', form = form, title = 'Edit journey %s' % journey.title, journey = journey, slides = slides)

# SLIDES

@app.route('/new-slide/<int:journey_id>', methods = ['GET', 'POST'])
@login_required
def new_slide(journey_id):
    journey = Journey.query.filter_by(id = journey_id, user_id = current_user.id).first()

    if not journey:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))

    form = NewSlideForm(journey_id = journey_id)

    if form.validate_on_submit():
        slide = Slide()
        slide.create(form.data['title'], form.data['description'], journey_id)
        db.session.add(slide)
        db.session.commit()
        flash('Slide added to journey', 'success')
        return redirect(url_for('index'))

    flash_errors(form)
    return render_template('new-slide.html', form = form, title = 'New Slide')

@app.route('/delete-slide/<int:slide_id>', methods = ['GET', 'POST'])
@login_required
def delete_slide(slide_id):
    slide = Slide.query.filter_by(id = slide_id).first()
    if not slide:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))
    journey = Journey.query.filter_by(id = slide.journey_id, user_id = current_user.id).first()
    if not journey:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))

    form = DeleteSlideForm(slide_id = slide.id)

    if form.validate_on_submit():
        Slide.query.filter(Slide.id == slide_id).delete()
        db.session.commit()
        flash('Slide successfully deleted.', 'success')
        return redirect(url_for('edit_journey', journey_id = journey.id))

    flash_errors(form)
    return render_template('delete-slide.html', form = form, slide = slide, title = 'Delete slide %s' % slide.title)

@app.route('/edit-slide/<int:slide_id>', methods = ['GET', 'POST'])
@login_required
def edit_slide(slide_id):
    slide = Slide.query.filter_by(id = slide_id).first()
    if not slide:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))
    journey = Journey.query.filter_by(id = slide.journey_id, user_id = current_user.id).first()
    if not journey:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))

    form = EditSlideForm(slide_id = slide_id, title = slide.title, description = slide.description)

    if form.validate_on_submit():
        slide.title = form.data['title']
        slide.description = form.data['description']
        db.session.commit()
        flash('Slide successfully updated.', 'success')
        return redirect(url_for('edit_journey', journey_id = journey.id))

    photos = Photo.query.filter_by(slide_id = slide_id)

    flash_errors(form)
    return render_template('edit-slide.html', form = form, title = 'Edit slide %s' % slide.title, slide = slide, photos = photos)

# PHOTOS

@app.route('/new-photo/<int:slide_id>', methods = ['GET', 'POST'])
@login_required
def new_photo(slide_id):
    slide = Slide.query.filter_by(id = slide_id).first()
    if not slide:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))
    journey = Journey.query.filter_by(id = slide.journey_id, user_id = current_user.id).first()
    if not journey:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))

    form = NewPhotoForm(slide_id = slide_id)

    if form.validate_on_submit():
        photo = Photo()
        tmp = tempfile.NamedTemporaryFile(suffix = '.jpg')
        form.photo.data.save(tmp)
        tmp.flush()
        photo.create(form.data['title'], form.data['description'], slide_id, tmp.name)
        db.session.add(photo)
        db.session.commit()
        flash('Photo added to slide', 'success')
        return redirect(url_for('edit_slide', slide_id = slide_id))

    flash_errors(form)
    return render_template('new-photo.html', form = form, title = 'New Photo')

@app.route('/edit-photo/<int:photo_id>', methods = ['GET', 'POST'])
@login_required
def edit_photo(photo_id):
    photo = Photo.query.filter_by(id = photo_id).first()
    if not photo:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))
    slide = Slide.query.filter_by(id = photo.slide_id).first()
    if not slide:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))
    journey = Journey.query.filter_by(id = slide.journey_id, user_id = current_user.id).first()
    if not journey:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))

    form = EditPhotoForm(photo_id = photo_id, title = photo.title, description = photo.description)

    if form.validate_on_submit():
        photo.title = form.data['title']
        photo.description = form.data['description']
        db.session.commit()
        flash('Photo successfully updated.', 'success')
        return redirect(url_for('edit_slide', slide_id = slide.id))

    flash_errors(form)
    return render_template('edit-photo.html', form = form, title = 'Edit photo %s' % photo.title, photo = photo)

@app.route('/delete-photo/<int:photo_id>', methods = ['GET', 'POST'])
@login_required
def delete_photo(photo_id):
    photo = Photo.query.filter_by(id = photo_id).first()
    if not photo:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))
    slide = Slide.query.filter_by(id = photo.slide_id).first()
    if not slide:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))
    journey = Journey.query.filter_by(id = slide.journey_id, user_id = current_user.id).first()
    if not journey:
        flash(BAD_KITTY, 'danger')
        return redirect(url_for('index'))

    form = DeletePhotoForm(photo_id = photo.id)

    if form.validate_on_submit():
        Photo.query.filter(Photo.id == photo_id).delete()
        db.session.commit()
        flash('Photo successfully deleted.', 'success')
        return redirect(url_for('edit_slide', slide_id = slide.id))

    flash_errors(form)
    return render_template('delete-photo.html', form = form, photo = photo, title = 'Delete photo %s' % photo.title)

# USERS

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    form = LoginForm()

    if form.validate_on_submit():
        user = User()
        if user.auth(form.data['login'], form.data['password']):
            login_user(user)
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
        try:
            user = User()
            user.create(form.data['login'], form.data['email'], form.data['password'])
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Account successfully created.', 'success')
            return redirect(url_for('index'))
        except:
            flash('This account is already registered.', 'danger')
            return redirect(url_for('register'))

    flash_errors(form)
    return render_template('register.html', form = form, title = 'Register')

@app.route('/me', methods = ['GET', 'POST'])
@login_required
def me():
    journeys = Journey.query.filter_by(user_id = current_user.id)
    return render_template('me.html', journeys = journeys, title = 'My Account')

@login_manager.unauthorized_handler
def unauthorized():
    flash('You need to sign in to access this page', 'danger')
    return redirect(login_url(url_for('login'), request.url))
