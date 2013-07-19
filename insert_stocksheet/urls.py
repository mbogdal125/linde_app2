from django.conf.urls import patterns, include, url
from insert_stocksheet.views import insertstockdata, chosestocksheet

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^chose_stocktaking/$', insertstockdata, name='chose-stocktaking'),
    url(r'^chose_stocksheet/(?P<stocktaking_number>\d+)$', chosestocksheet, name='chose-stocksheet'),
    # Examples:
    # url(r'^linde_app2/', include('linde_app2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)