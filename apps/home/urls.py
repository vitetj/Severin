from django.conf.urls import *
from . import views

#si on tape rien on arrive sur l'accueil
#si y'a juste un truc on vas dire qu'on appel une page, si on la trouve pas on cherche au niveau des package dispo, sinon errueur 404
urlpatterns = [
    url(r'^$', views.index),
    url(r'^contact$', views.contact),
]
