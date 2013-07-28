from django.conf.urls import patterns, include, url
from linde_returns.views import chosestocktaking, chosestocksheet, returnstocksheet

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^chose_stocktaking/$', chosestocktaking, name='returns-chose-stocktaking'),
    url(r'^chose_stocksheet/(?P<stocktaking_number>\d+)$', chosestocksheet, name='returns-chose-stocksheet'),
    url(r'^stocksheet_return/(?P<stocksheet_number>\d+)$', returnstocksheet, name='return-stocksheet'),
    # Examples:
    # url(r'^linde_app2/', include('linde_app2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
