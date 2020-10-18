# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, Image

# Create your views here.
@login_required(login_url='/accounts/login/')
def photos(request):
    posts=Profile.save_profile()
    photos=Image.save_image()
    return render(request, 'posts.html',{"photos":photos, "posts":posts})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


    