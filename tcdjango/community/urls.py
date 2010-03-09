from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'domain/(?P<domain>\w+)/$', 'tcdjango.community.views.home'),
    (r'', 'tcdjango.community.views.home'),


)
