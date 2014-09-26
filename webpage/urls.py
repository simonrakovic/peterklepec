__author__ = 'user'

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^fitnes/', 'webpage.views.fitnes', name='home'),
    url(r'^cenik/', 'webpage.views.pricelist', name='home'),
    url(r'^urnik/', 'webpage.views.timetable', name='home'),
    url(r'^$', 'webpage.views.home', name='home'),

                       )