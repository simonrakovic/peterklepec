import os
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
from peterklepec_webpage import settings

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'peterklepec_webpage.views.home', name='home'),
    # url(r'^peterklepec_webpage/', include('peterklepec_webpage.foo.urls')),
    url(r'^', include('webpage.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^images/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    # Uncomment the next line to enable the admin:
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),



    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    (r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml')),
)
