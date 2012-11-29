from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import messages
from bookmarks.models import Bookmark
from bookmarks.forms import BookmarkForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core import serializers
import json
from datetime import datetime

def index(request):
    bookmarks = Bookmark.objects.filter(pub_date__lte=datetime.utcnow).order_by('-pub_date')[:10]
    return render_to_response('index.html', 
                                {'bookmarks': bookmarks}, 
                                context_instance=RequestContext(request))

def details(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    return render_to_response('bookmark_details.html', 
                                {'bookmark': bookmark}, 
                                context_instance=RequestContext(request))

@login_required
def show_user_bookmarks(request):
    bookmarks = Bookmark.objects.filter(author=request.user)
    return render_to_response('show_user_bookmarks.html', 
                                {'bookmarks': bookmarks}, 
                                context_instance=RequestContext(request))

@login_required
def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.author = request.user
            bookmark.save()
            return render_to_response('add_bookmark_thanks.html', 
                                        context_instance=RequestContext(request))
    else:
        form = BookmarkForm()
        
    return render_to_response('add_bookmark.html', 
                                {'form':form}, 
                                context_instance=RequestContext(request))


@login_required
def vote(request, bookmark_id, direction):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    getattr(bookmark, direction)() # dynamically call the right direction
    bookmark.save()
    result = bookmark.votes
    if request.is_ajax():
        json_data = json.dumps({'votes' : result })
        return HttpResponse(json_data, mimetype='application/json')
    else:
        return render_to_response('vote_result.html', 
                                    {'result': result }, 
                                    context_instance=RequestContext(request))

@login_required
def modify(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id, author=request.user)
    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.author = request.user
            bookmark.save()
            messages.success(request, 'Bookmark details updated.')
            return HttpResponseRedirect('/bookmark/%s/'%bookmark_id)
        else:
            return render_to_response('bookmark_modify.html', 
                                        {'bookmark_id': bookmark_id, 'form': form}, 
                                        context_instance=RequestContext(request))
    else:
        form = BookmarkForm(instance=bookmark)
        return render_to_response('bookmark_modify.html', 
                                    {'bookmark_id': bookmark_id, 'form': form}, 
                                    context_instance=RequestContext(request))

@login_required
def delete(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id, author=request.user)
    bookmark.delete()
    messages.success(request, 'Bookmark successfully deleted.')
    return HttpResponseRedirect('/bookmark/show_mine/')
