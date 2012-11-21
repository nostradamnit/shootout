from bookmarks.models import Bookmark
from django.contrib.auth.models import User

from django.test import TestCase


class BookmarkTests(TestCase):
    
    def setUp(self):
        author = User.objects.create(username='blah', password='blah')
        self.bookmark = Bookmark.objects.create(url='http://s.it/', title='sit site', description='sit site, duh', author=author, votes=0)
        
    
    def test_can_upvote(self):
        self.assertEqual(self.bookmark.votes, 0)
        self.bookmark.upvote()
        self.assertEqual(self.bookmark.votes, 1)
        self.bookmark.downvote()
        self.assertEqual(self.bookmark.votes, 0)
