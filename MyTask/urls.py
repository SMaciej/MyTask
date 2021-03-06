from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tasks.views.home', name='home'),
    url(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^logout/', 'django.contrib.auth.views.logout'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
