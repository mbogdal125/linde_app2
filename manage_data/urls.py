from django.conf.urls import patterns, include, url
from manage_data.views import customers, add_customer

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^listcustomers/$', customers , name='list-customers'),
    url(r'^addcustomer/$', add_customer , name='add-customer'),

)
