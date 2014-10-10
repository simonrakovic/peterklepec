
import webpage

from webpage import views

__author__ = 'user'

from django.conf.urls import patterns, include, url



urlpatterns = patterns('',

        url(r'^ponudba/(?P<id>\d+)/$', 'webpage.views.offers', name='home'),
        url(r'^novice/(?P<id>\d+)/$', 'webpage.views.custompage', name='home'),
        url(r'^cenik/$', 'webpage.views.pricelist', name='home'),
        url(r'^urnik/(?P<id>\d+)/$', 'webpage.views.timetable', name='home'),
        url(r'^informacije/$', 'webpage.views.info', name='home'),
        url(r'^$', 'webpage.views.home', name='home'),
        url(r'^casizvajanjavadb/(?P<id>\d+)/$', views.ExercisesWeeklyTimetableList.as_view() , name='timetable-list'),
        url(r'^odsotnosti/(?P<id>\d+)/$', views.NotWorkingHoursList.as_view() , name='timetable-list'),
    )