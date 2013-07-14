from django.conf.urls import patterns, include, url
from manage_users.views import listUser

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^listuser/$', listUser , name='list-user'),

)
