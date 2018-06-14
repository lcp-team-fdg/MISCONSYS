
#=====================================#
#   Url routing for the application   #
#  Allows for routing of the app to   #
#  function properly                  #
#                                     #
#         Author: David Kroell        #
#        Version: 03/01/2018          #
#                                     #
#=====================================#

# -- Import dependencies
from django.conf.urls import url
from . import views

# -- Different routes that are possible to access.
urlpatterns = [
    url(r'^$', views.index, name='index'),

    # Begin the url api we need.
    url(r'^api/images/$', views.images, name='images'),
    url(r'^api/targets/$', views.targets, name='targets'),
]
