from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'bookmarks.views.index', name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^bookmark/show_mine/$', 'bookmarks.views.show_user_bookmarks'),
    url(r'^bookmark/add/$', 'bookmarks.views.add_bookmark'),
    url(r'^bookmark/(?P<bookmark_id>\d+)/$', 'bookmarks.views.details'),
    url(r'^bookmark/(?P<bookmark_id>\d+)/upvote/$', 'bookmarks.views.upvote'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
