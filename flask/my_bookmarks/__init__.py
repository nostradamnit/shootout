from __future__ import with_statement
from contextlib import closing
import hashlib
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

 
# configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/my_bookmarks-sqlalchemy.db' % os.path.dirname(os.path.abspath(__file__))
DEBUG = True
SECRET_KEY = 'randomcharacters'


app = Flask('my_bookmarks')
app.config.from_object(__name__)
db = SQLAlchemy(app)

def init_db():
    db.create_all()

def create_admin(username, password, email):
    from models import User
    admin = User(username, password, email)
    db.session.add(admin)
    db.session.commit()

import views
