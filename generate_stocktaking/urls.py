from django.conf.urls import patterns, include, url
from generate_stocktaking.views import generate_stocktaking
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^gen_stocktaking/$', generate_stocktaking , name='generate-stocktaking'),

)
