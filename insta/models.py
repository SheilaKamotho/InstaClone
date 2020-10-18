# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/', null=True)
    name = models.CharField(max_length = 60, null=True)
    bio = models.TextField(null=True)

    def save_profile(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'image/', null=True)
    name = models.CharField(max_length = 60)
    caption = models.TextField()
    likes = models.IntegerField()
    comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_image(self):
        self.save()

    @classmethod
    def save_image(cls):
        images=cls.objects.save()
        return images