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

