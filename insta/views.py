# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Image
from .forms import NewImageForm,NewProfileForm

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

def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect('photos')
        
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form":form, "current_user":current_user})

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('profile')
        
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form":form, "current_user":current_user})

def profile(request):
    posts=Profile.save_profile()
    photos=Image.save_image()
    return render(request, 'profile.html',{"photos":photos, "posts":posts})





    