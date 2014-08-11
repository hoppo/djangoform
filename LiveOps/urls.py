from django.conf.urls import patterns, include, url
from LiveOps.views import * 
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', homepage),
    url(r'^report/$', report),
    url(r'^search/$', search),
    url(r'^search/(\d+)/$', display_report),
    url(r'^report/added/$', added),

    url(r'^admin/', include(admin.site.urls)),
)
