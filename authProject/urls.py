from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'authProject.views.home', name='home'),
    # url(r'^authProject/', include('authProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^register/$','authSystem.views.UserRegistration')
)
