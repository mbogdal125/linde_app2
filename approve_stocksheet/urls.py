from django.conf.urls import patterns, include, url
from approve_stocksheet.views import chosestocktaking, chosestocksheet

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^chose_stocktaking/$', chosestocktaking, name='approve-chose-stocktaking'),
    url(r'^chose_stocksheet/(?P<stocktaking_number>\d+)$', chosestocksheet, name='approve-chose-stocksheet'),
#    url(r'^agreedata/(?P<stocksheet_number>\d+)$', agreestocksheetdata, name='agree-stocksheetdata'),
    # Examples:
    # url(r'^linde_app2/', include('linde_app2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
