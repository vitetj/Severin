from django.conf.urls import *
from . import views


urlpatterns = [
    url(r'vps/$', views.pageVps, name="vps"),
    url(r'^web/$', views.pageWeb, name="web"),
]
