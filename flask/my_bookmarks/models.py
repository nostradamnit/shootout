from my_bookmarks import db, SECRET_KEY
from tools import hash_password

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(132))
    
    def __init__(self, username, password, email):
        self.username = username
        self.password = hash_password(username, password)
        self.email = email
        
    def __repr__(self):
        return '<User %r>' % self.username
        
class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('author', lazy='dynamic'))
    
    def __init__(self, url, description, pub_date, author):
        self.url = url
        self.description = description
        self.pub_date = pub_date
        self.author = author
        
    def __repr__(self):
        return '<Entry (%r)(%r)>' % self.id, self.url
