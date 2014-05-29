from models import User
from app import login_manager
from flask import flash

@login_manager.user_loader
def load_user(u):
    return u

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u'Error in the %s field - %s' % (getattr(form, field).label.text, error), 'danger')

