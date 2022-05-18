from django import shortcuts
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import user_profile
from .forms import UserForm, User_ProfileForm
# Create your views here.

def feed (request):
    if request.user.is_authenticated:
        return render(request, 'feed.html')
    else:
        return render(request, 'home.html')


def home (request):
    if request.user.is_authenticated:
        return render(request, 'feed.html')
    else: 
        return render(request, 'home.html')

def register(request):
    if request.method =='POST':
        user = UserForm(request.POST, prefix= "user")
        profile = User_ProfileForm(request.POST, prefix="userprofile")
        if user.is_valid() and profile.is_valid():
            user = user.save()
            user_profile = user_profile.save(commit=False)
            user_profile.user = user
            user_profile.save()
            return HttpResponseRedirect('home.html')
    else:
        user = UserForm(request.POST, prefix= "user")
        profile = User_ProfileForm(request.POST, prefix="userprofile")
        return render(request,'register.html',{'UserForm':UserForm,'User_ProfileForm':User_ProfileForm})
        