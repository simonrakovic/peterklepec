import os
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import xadmin
from peterklepec_webpage import settings

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'peterklepec_webpage.views.home', name='home'),
    # url(r'^peterklepec_webpage/', include('peterklepec_webpage.foo.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^', include('webpage.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^images/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    # Uncomment the next line to enable the admin:
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),

)
