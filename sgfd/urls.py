#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings

from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sgfd.views.home', name='home'),
    # url(r'^sgfd/', include('sgfd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', 'login.views.home'),    
    (r'^cadastro', 'login.views.cadastro'),
    (r'^perfil', 'login.views.perfil'),
    (r'^logout', 'login.views.sair'),
    
    
    (r'^admin/', include(admin.site.urls)),    
    
    # media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
)
