# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import *
from blog import views


#urlpatterns = patterns(('blog.views'),
urlpatterns = [
    url(r'^bloglist/$',views.blog_list),
    url(r'^(?P<id>\d+)/$',views.blog_show,name='blog_show'),
   # url(r'^search/$',            'blog_search',     name='blog_search'),
    url(r'^category/(?P<id>\d+)/$', views.blog_category,name='blog_category'),
    url(r'^Article/Gt(.{,3})/$',views.GetCategory), #admin修改文章页面用的
]