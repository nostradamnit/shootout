from flask import request, session, g, redirect, url_for, abort, render_template, flash
from sqlalchemy.exc import IntegrityError
from my_bookmarks import db, app
from models import User, Bookmark
from datetime import datetime
from forms import LoginForm, RegistrationForm, BookmarkForm
from tools import hash_password

@app.route('/')
def show_bookmarks():
    form = BookmarkForm(request.form)
    bookmarks = Bookmark.query.all()
    return render_template('show_bookmarks.html', bookmarks=bookmarks, form=form)
    
@app.route('/add', methods=['POST'])
def add_bookmark():
    if not session.get('logged_in'):
        abort(401)
    form = BookmarkForm(request.form)
    if request.method == 'POST' and form.validate():
        if form.url.data and form.description.data:
            author = User.query.filter_by(username=session.get('username')).first()
            bookmark = Bookmark(form.url.data, form.description.data, datetime.utcnow(), author)
            db.session.add(bookmark)
            db.session.commit()
            flash('New bookmark saved successfully')
        else:
            flash('URL is required.')
    return redirect(url_for('show_bookmarks'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data, password=hash_password(form.username.data, form.password.data)).first()
        if user:
            session['logged_in'] = True
            session['username'] = user.username
            flash('you are logged in')
            return redirect(url_for('show_bookmarks'))
        else:
            print 'user not found'

    return render_template('login.html', error=error, form=form)
    
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('you were logged out')
    return redirect(url_for('show_bookmarks'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data, form.email.data)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            error = 'Username already exists, please choose another'
            db.session.rollback()
        if not error:
            flash('Your account has been created.')
            flash('You may now log in')
            return redirect(url_for('show_bookmarks'))
    return render_template('registration.html', form=form, error=error)
