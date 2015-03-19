# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from rest_framework import routers
from views import IndexView, ResolutionList, ResolutionDetail

#router = routers.DefaultRouter()
#router.register(r'resolution', ResolutionList.as_view(), 'resolution')


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^api/', include(router.urls, namespace='api')),
    #url(r'^', include(router.urls)),
    url(r'^api/resolution/$', ResolutionList.as_view(), name='resolution-list'),
    url(r'^api/resolution/(?P<pk>[0-9]+)$', ResolutionDetail.as_view(), name='resolution-detail'),
)
