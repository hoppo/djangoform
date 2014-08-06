from django.conf.urls import patterns, include, url
from LiveOps.views import * 
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', homepage),
    url(r'^test/$', test), 
    url(r'^hello/$', hello),
    url(r'^report/$', report),
    url(r'^search/$', search),
    url(r'^display_meta/$', display_meta),
    url(r'^report/added/$', added),
    # Examples:
    # url(r'^$', 'LiveOps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
