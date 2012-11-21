from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    url = models.CharField(max_length=500)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.url
        
    def get_absolute_url(self):
        return ('bookmark_detail', (), {'bookmark_id' : self.pk})
        
    def upvote(self):
        self.votes = self.votes + 1
        self.save()
        
    def downvote(self):
        self.votes = self.votes - 1
        self.save()
