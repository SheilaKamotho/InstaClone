# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ProfileClass(TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_profile=Profile(bio = 'Sheila is becoming a world class software developer')

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_update_method(self):
        self.new_profile.save_profile()
        self.new_profile= Profile.objects.filter(id==1).update()
        self.updated_profile=Profile.objects.get(id==1)
        self.assertTrue(self.updated_profile.img,'posts')

    def test_profile_delete(self):
        self.profile.save_profile()
        self.searched_profile = Profile.objects.get(id==1)
        self.searched_profile.delete_image()
        self.assertTrue(len(Profile.objects.all()) == 0)

class ImageClass(TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_profile=Profile(bio='World Class Software Developer')
        self.new_profile.save_profile()

        self.new_image=Image(name='Sheila',caption='a beautiful day',likes=2,comments='Looking sharp',profile=self.new_profile)
        self.new_image.save

    def test_instance(self):
        '''
        Test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        '''
        Test case to test the save functionality
        '''
        self.new_image.save()
        image=Image.objects.all()
        self.assertTrue(len(image)>0)

    def test_image_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_image_update(self):
       self.image.save_image()
       self.image=Image.objects.filter(id==1).update() 
       self.updated_image=Image.objects.get(id==1)
       self.assertTrue(self.updated_image.img,'photos')


    def test_image_delete(self):
        self.image.save_image()
        self.searched_image = Image.objects.get(id==1)
        self.searched_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_search_image_category(self):
        self.image.save_image()
        self.name= Name(name='sheila')
        self.name.save_name()
        self.searched_images=Image.search_by_name('sheila')
        self.assertTrue(len(self.searched_images) > 0)

    