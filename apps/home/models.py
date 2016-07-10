#-*- coding: utf-8 -*-
#TODO verifier quelle
from django.db import models
from tinymce.models import HTMLField
import os

class Page(models.Model):
    label = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = HTMLField(default='contenu')

class Article(models.Model):
    label = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = HTMLField(default='contenu')

class Tag(models.Model):
    label = models.CharField(max_length=200)

#class Realisation(models.Model):
#    id = models.AutoField()
#    name = models.CharField(max_length=200)
#    description = models.TextField()
#    adressWeb = models.CharField(max_length=200)
#    client = models.CharField(max_length=200)
#    photos = models.CharField(max_length=200)
