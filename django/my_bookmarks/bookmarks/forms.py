from django.forms import ModelForm
from bookmarks.models import Bookmark

class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        exclude = ['author', 'votes']
