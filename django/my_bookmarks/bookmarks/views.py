from django.shortcuts import render_to_response
from bookmarks.models import Bookmark
from bookmarks.forms import BookmarkForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core import serializers
import json
from datetime import datetime

def index(request):
    bookmarks = Bookmark.objects.filter(pub_date__lt=datetime.utcnow).order_by('-pub_date')
    return render_to_response('index.html', {'bookmarks': bookmarks}, context_instance=RequestContext(request))

@login_required
def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.author = request.user
            bookmark.save()
            return render_to_response('add_bookmark_thanks.html')
    else:
        form = BookmarkForm()
        
    return render_to_response('add_bookmark.html', {'form':form}, context_instance=RequestContext(request))
    
@login_required
def show_user_bookmarks(request):
    bookmarks = Bookmark.objects.filter(author=request.user)
    return render_to_response('show_user_bookmarks.html', {'bookmarks': bookmarks})

@login_required
def upvote(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    bookmark.upvote()
    bookmark.save()
    result = bookmark.votes
    if request.is_ajax():
        json_data = json.dumps({'upvotes' : result })
        return HttpResponse(json_data, mimetype='application/json')
    else:
        return render_to_response('upvote_result.html', {'result': result }, context_instance=RequestContext(request))

def details(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    return render_to_response('bookmark_details.html', {'bookmark': bookmark}, context_instance=RequestContext(request))
