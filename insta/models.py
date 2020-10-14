# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/', null=True)
    bio = models.TextField()

class Image(models.Model):
    image = models.ImageField(upload_to = 'image/', null=True)
    name = models.CharField(max_length = 60)
    caption = models.TextField()
    likes = models.IntegerField()
    comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)