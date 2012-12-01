from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from bookmarks.views import TenMostRecentBookmarks, TenMostPopularBookmarks, BookmarkDetail
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', TenMostRecentBookmarks.as_view(), name='index'),
    url(r'^popular/$', TenMostPopularBookmarks.as_view(), name='popular'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^bookmark/show_mine/$', 'bookmarks.views.show_user_bookmarks'),
    url(r'^bookmark/add/$', 'bookmarks.views.add_bookmark'),
    url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDetail.as_view(), name='bookmark_detail'),
    url(r'^bookmark/(?P<bookmark_id>\d+)/modify/$', 'bookmarks.views.modify'),
    url(r'^bookmark/(?P<bookmark_id>\d+)/delete/$', 'bookmarks.views.delete'),
    url(r'^bookmark/(?P<bookmark_id>\d+)/(?P<direction>(up|down)vote)/$', 'bookmarks.views.vote'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
