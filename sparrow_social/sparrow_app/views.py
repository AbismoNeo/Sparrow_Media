from django import shortcuts
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import user_profile, message
from .forms import UserForm, User_ProfileForm
# Create your views here.

################# FEED VIEW #################
def feed (request):
    if request.user.is_authenticated:
        
        return render(request, 'feed.html')
    else:
        return render(request, 'home.html')

################# HOME VIEW #################
def home (request):
    if request.user.is_authenticated:
        posts = message.objects.all()
        profiles = user_profile.objects.all()
        # for profile in profiles:
        #     if posts.user_id == profiles.user:
        #         profiles = profile.objects.all()
        #         break
        #     else:
        #         continue
        context ={'posts':posts,'profiles':profiles}
        return render(request, 'feed.html',context)
    else: 
        return render(request, 'home.html')

################# REGISTER VIEW #################
def register(request):
    if request.method =='POST':
        user = UserForm(request.POST, prefix= "user")
        profile = User_ProfileForm(request.POST, prefix="userprofile")
        
        print(user)
        print(profile)
        if user.is_valid() and profile.is_valid() and user.password1 and user.password2 and user.password1==user.password2:            
            user = user.save()
            user_profile = user_profile.save(commit=False)
            user_profile.user = user
            user_profile.save()
            return HttpResponseRedirect('home.html')
    else:
        user = UserForm(request.POST, prefix= "user")
        profile = User_ProfileForm(request.POST, prefix="userprofile")
        print(user)
        print(profile)
        return render(request,'register.html',{'UserForm':UserForm,'User_ProfileForm':User_ProfileForm})

        