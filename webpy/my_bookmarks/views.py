import web
from forms import login_form, registration_form, bookmark_form
from models import User, Bookmark
from server import db, session

render = web.template.render('templates/', base='layout', globals={'context': session})


class index(object):
    def GET(self):
        return render.index()
        
class my_bookmarks(object):
    def GET(self):
        return 'My Bookmarks'
        
class add_bookmark(object):
    def GET(self):
        form = bookmark_form()
        content = 'Add bookmark'
        return render.add_bookmark(content, form)
    
    def POST(self):
        form = bookmark_form()
        if not form.validates():
            content = 'Validation error'
            return render.add_bookmark(content, form)
        else:
            i = web.input()
            #db = web.database(dbn='sqlite', db='bookmarks_webpy.sqlite')
            bookmark = Bookmark(db)
            bookmark.url = i.url
            bookmark.description = i.description
            bookmark.author = session.user_id
            result = bookmark.save()
            content = 'bookmark added'
            return render.add_bookmark_success(content, result)
        
class register(object):
    def GET(self):
        form = registration_form()
        content = 'Registration Form'
        return render.register(content, form)
    
    def POST(self):
        form = registration_form()
        if not form.validates():
            content = 'Registration error'
            return render.register(content, form)
        else:
            i = web.input()
            #db = web.database(dbn='sqlite', db='bookmarks_webpy.sqlite')
            user = User(db)
            user.username = i.username
            user.password = i.password
            user.email = i.email
            result = user.save()
            session.user_id = result
            content = 'registration successful'
            return render.register_success(content, result)
        
class login(object):
    def GET(self):
        form = login_form()
        content = 'Login Form'
        return render.login(content, form)
        
    def POST(self):
        form = login_form()
        if not form.validates():
            content = 'login error'
            return render.login(content, form)
        else:
            i = web.input()
            user = User(db)
            results = user.login(i.username, i.password)
            if results:
                for user in results:
                    print user.username
                    session.user_id = user.id
                return render.index()
            else:
                content = 'login failure'
                return render.login(content, form)
