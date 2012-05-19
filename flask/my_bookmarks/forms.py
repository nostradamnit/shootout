from wtforms import Form, TextField, PasswordField, BooleanField, validators
from flaskext.wtf.html5 import EmailField
from wtforms.ext.sqlalchemy.orm import model_form
from models import User, Bookmark

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')
    
    
class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=2, max=25)])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('password_confirm', message='Passwords must match')
    ])
    password_confirm = PasswordField('Confirm password')
    email = EmailField('Email', [validators.Length(min=5, max=135)])

BookmarkForm = model_form(Bookmark, Form)
