# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Image, Comment
from .forms import NewImageForm,NewProfileForm,NewCommentForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def photos(request):
    all_images = Image.objects.all()
    posts=Profile.save_profile()
    # photos=Image.save_image()
    comment=Comment.save_comment()
    comment = Comment.objects.all()
    # test = dir(all_images)
    # print(test)
    return render(request, 'posts.html',{"all_images":all_images, "posts":posts, "comment":comment})

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

def new_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.editor = current_user
            comment.save()
        return redirect('photos')
        
    else:
        form = NewCommentForm()
    return render(request, 'new_comment.html', {"form":form, "current_user":current_user})


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





    