

class User(object):
    def __init__(self, db = None):
        self.db = db
        print self.db.ctx
        
    @property
    def username(self):
        return self._username
        
    @username.setter
    def username(self, value):
        self._username = value
        
    @property 
    def password(self):
        return 'secret'
        
    @password.setter
    def password(self, value):
        self._password = value
        
    @property
    def email(self):
        return self._email
        
    @email.setter
    def email(self, value):
        self._email = value
        
    @property
    def id(self):
        return self._id
        
    def login(self, username, password):
        where = "username = '%s' and password = '%s'" % (username, password)
        results = self.db.select('user', where=where)
        return results
        
    def save(self):
        if self.db:
            result = self.db.insert('user',  username=self._username, password=self._password, email=self._email)
            self._id = result
            return result
    
class Bookmark(object):
    def init(self, db = None):
        if db:
            self.db = db
    
    @property
    def url(self):
        return self._url
        
    @url.setter
    def url(self, value):
        self._url = value
        
    @property
    def description(self):
        return self._description
        
    @description.setter
    def description(self, value):
        self._description = value
        
    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, value):
        self._author = value.id
        
    @property
    def pub_date(self):
        return self._pub_date
        
    @property 
    def id(self):
        return self._id
        
    def save(self):
        if self.db:
            result = self.db.insert('bookmark',  url=self._url, description=self._description, author_id=self._author)
            self._id = result
            return result
        
