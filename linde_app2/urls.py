from django.conf.urls import patterns, include, url
from linde_app2.views import home_page, stocktaking, stocksheet
from manage_users.views import listUser

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home_page, name='home'),
    url(r'^(?P<page_number>\d+)$', home_page, name='home'),
    url(r'^stocktaking/(?P<stocktaking_number>\d+)$', stocktaking, name='stocktaking'),
    url(r'^stocksheet/(?P<stocksheet_number>\d+)$', stocksheet, name='stocksheet'),


    url(r'^users/', include('manage_users.urls')),
    url(r'^manage_data/', include('manage_data.urls')),
    url(r'^stocktakings/', include('generate_stocktaking.urls')),
    url(r'^insert/', include('insert_stocksheet.urls')),
    # url(r'^linde_app2/', include('linde_app2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
