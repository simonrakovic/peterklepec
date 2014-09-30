__author__ = 'user'

from django.conf.urls import patterns, include, url



urlpatterns = patterns('',

    url(r'^ponudba/(?P<id>\d+)/$', 'webpage.views.offers', name='home'),


    url(r'^cenik/', 'webpage.views.pricelist', name='home'),
    url(r'^urnik/', 'webpage.views.timetable', name='home'),
    url(r'^$', 'webpage.views.home', name='home'),

    )