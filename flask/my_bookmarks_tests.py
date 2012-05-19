import os
import my_bookmarks
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, self.tmp_file = tempfile.mkstemp()
        my_bookmarks.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % self.tmp_file
        self.app = my_bookmarks.app.test_client()
        my_bookmarks.init_db()
        my_bookmarks.create_admin('admin','pass','sam@samcranford.com')
        
    def tearDown(self):
        os.close(self.db_fd)    
        os.unlink(self.tmp_file)
        
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
            ), follow_redirects=True)
        
    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert rv.status_code == 200, 'Request successful'
        assert 'no bookmarks' in rv.data    

    def test_create_bookmark(self):
        self.login('admin', 'pass')
        rv = self.app.post('/add', 
            data=dict(url='http://localhost/', description='localhost'), 
            follow_redirects=True)
        assert 'New bookmark saved successfully' in rv.data
    
    def test_create_empty_bookmark_fail(self):
        self.login('admin', 'pass')
        rv = self.app.post('/add', 
            data=dict(url='', description=''), 
            follow_redirects=True)
        assert 'URL is required.' in rv.data
        
    def test_registration(self):
        rv = self.app.post('/register', data=dict(
            username='anon', password='ymous', password_confirm='ymous', email='not@anonymous.com'), 
            follow_redirects=True)
        assert 'Your account has been created' in rv.data
        
    def test_registration_duplicate_username(self):
        self.test_registration()
        rv = self.app.post('/register', data=dict(
            username='anon', password='ymous', password_confirm='ymous', email='not@anonymous.com'), 
            follow_redirects=True)
        assert 'Username already exists, please choose another' in rv.data
        
if __name__ == '__main__':
    unittest.main()
