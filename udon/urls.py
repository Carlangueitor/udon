from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   url(r'^admin/', include(admin.site.urls)),
   url(r'^$', direct_to_template, { 'template': 'home.jade' }, 'index'),
   url(r'^login/', 'django.contrib.auth.views.login', { 'template_name': 'login.jade' }, 'login'),
)
