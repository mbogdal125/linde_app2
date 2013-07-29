#-*- coding: utf-8 -*
from django.conf.urls import patterns, include, url
from manage_data.views import customers, add_customer, gas_types, add_gas_type, gas_groups, add_gas_group
from django.contrib.auth.decorators import login_required

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^listcustomers/(?P<numpage>\d+)$', login_required(customers), name='list-customers'),
    url(r'^listcustomers/$', login_required(customers), name='list-customers'),
    url(r'^addcustomer/$', login_required(add_customer), name='add-customer'),
    url(r'^gastypes/$', login_required(gas_types), name='list-gastypes'),
    url(r'^addgastypes/$', login_required(add_gas_type), name='add-gastype'),
    url(r'^gasgroups/$', login_required(gas_groups), name='list-gasgroups'),
    url(r'^addgasgroup/$', login_required(add_gas_group), name='add-gasgroup'),

)
