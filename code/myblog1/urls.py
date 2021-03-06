from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls import patterns, include, url
from myblog import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^index/$',views.index_page),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^blog/(?P<id>\d+)/$', views.blog_show, name='detail_blog'),
    url(r'^index',views.index_page,name='RSS_url'),
    url(r'^(?P<id>\d+)/commentshow/$', 'blog_show_comment', name='showcomment'),
    url(r'^addblog/',views.add_blog,name='add_blog'),
    url(r'^addblogact/',views.add_blog_action,name='add_blog'),

)
