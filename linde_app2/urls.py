from django.conf.urls import patterns, include, url
from linde_app2.views import home_page, stocktaking, stocksheet
from django.contrib.auth.decorators import login_required
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', home_page, name='home'),
    url(r'^$', login_required(home_page), name='home'),
    url(r'^(?P<page_number>\d+)$', login_required(home_page), name='home'),
    url(r'^stocktaking/(?P<stocktaking_number>\d+)$', login_required(stocktaking), name='stocktaking'),
    url(r'^stocksheet/(?P<stocksheet_number>\d+)$', login_required(stocksheet), name='stocksheet'),

    url(r'^manage_data/', include('manage_data.urls')),
    url(r'^stocktakings/', include('generate_stocktaking.urls')),
    url(r'^insert/', include('insert_stocksheet.urls')),
    url(r'^agree/', include('agree_stocksheet.urls')),
    url(r'^approve/', include('approve_stocksheet.urls')),
    url(r'^returns/', include('linde_returns.urls')),
    url(r'^login/$',  'django.contrib.auth.views.login', {'template_name':'login.html'}, name="login"),
    url(r'^logout/$',  'django.contrib.auth.views.logout', {'template_name':'logout.html'}, name="logout"),
    # url(r'^registration/', include('registration.urls')), 
    # url(r'^auth/', include('registration.auth_urls')), 
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^linde_app2/', include('linde_app2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
