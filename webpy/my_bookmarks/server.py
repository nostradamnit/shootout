import web
import views
from urls import urls

db = web.database(dbn='sqlite', db='bookmarks_webpy.sqlite')
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})


if __name__ == "__main__":    
    app.run()
