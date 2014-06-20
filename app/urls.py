from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^about/', 'app.views.about', name='about'),
    url(r'^careers/', 'app.views.careers', name='careers'),
    url(r'^leadership/', 'app.views.leadership', name='leadership'),
    url(r'^community/', 'app.views.community', name='community'),
    url(r'^news/', 'app.views.news', name='news'),
    url(r'^contact/', 'app.views.contact', name='contact'),
    url(r'^robots\.txt', 'app.views.robots', name='robots'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
