from django.conf.urls import patterns, include, url
from manage_data.views import customers, add_customer, gas_types, add_gas_type, gas_groups, add_gas_group

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^listcustomers/$', customers , name='list-customers'),
    url(r'^addcustomer/$', add_customer , name='add-customer'),
    url(r'^gastypes/$', gas_types , name='list-gastypes'),
    url(r'^addgastypes/$', add_gas_type , name='add-gastype'),
    url(r'^gasgroups/$', gas_groups , name='list-gasgroups'),
    url(r'^addgasgroup/$', add_gas_group , name='add-gasgroup'),

)
