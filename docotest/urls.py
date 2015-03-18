# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from views import ResolutionList

router = routers.DefaultRouter()
router.register(r'resolution', ResolutionList)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'docotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'docotest.views.index', name='index'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include(router.urls, namespace='api')),


)
