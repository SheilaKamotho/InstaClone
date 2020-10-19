# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/', null=True)
    name = models.CharField(max_length = 60, null=True)
    editor = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)

    def save_profile(self):
        self.save()

    @classmethod
    def save_profile(cls):
        posts=cls.objects.filter()
        return posts

    def update_profile(self):
        self.update()

    def delete_profile():
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'image/', null=True)
    name = models.CharField(max_length = 60)
    caption = models.TextField()
    likes = models.IntegerField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    comments = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_image(self):
        self.save()

    @classmethod
    def save_image(cls):
        photos=cls.objects.filter()
        return photos

    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos
    
    def update_image(self):
        self.update()

    def delete_image():
        self.delete()
  

        
    