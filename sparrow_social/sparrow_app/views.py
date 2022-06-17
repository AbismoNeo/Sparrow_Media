from django import shortcuts
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext
from .models import user_profile, message, list_follow
from .forms import UserForm, User_ProfileForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User as user
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

################# home VIEW #################
def home (request):
    if request.user.is_authenticated:
        ####### AQUI SE VEN LAS NOTICIAS (POSTEOS DE ADMIN) #########
        news = message.objects.filter(user_id__username ='admin')
        ####### AQUI SE VE LOS SEGUIDORES Y A LOS QUE SEGUIMOS #########
        try:
            list_friendship = list_follow.objects.filter(id_list = request.user)
            list_friend_count = list_friendship.count() 
        except:
            list_friend_count = 0
        try:    
            
            list_following = list_follow.objects.filter(id_friend = request.user)
            list_follow_count = list_following.count()
        except:
            list_follow_count = 0
        print("Following %s", list_follow_count)
        print("Followers %s", list_friend_count)
        ####### AQUI SE VE LOS POST QUE VEREMOS #########
        postslist = message.objects.all()
        profilelist= user_profile.objects.all()
        postbox = PostForm(request.POST)
        user_data = profilelist.get( user = request.user.id)
        ####### AQUI SE HACEN LOS POST NUEVOS #########
        if request.method =='POST':
            if postbox.is_valid():
                postbox.instance.user_id = request.user
                try:
                    postbox.save()
                    messages.success(request,'Post actualizado correctamente!')
                except:
                    messages.error(request,'Post no realizado correctamente!')
                return redirect('home')
        else:
            form = PostForm()
        context ={'postslist':postslist,'profilelist':profilelist, 'user_data': user_data, 'Form':form,'list_follow_count':list_follow_count,'list_friend_count':list_friend_count,'news':news}
            #context ={'postslist':postslist,'Form':form}
        return render(request, 'home.html', context)
    else:
        return redirect('login')


################# REGISTER VIEW #################
@csrf_exempt
def register(request):
    user = UserForm(request.POST)
    user_profile = User_ProfileForm(request.POST, request.FILES)
    print(request.FILES)
    if request.method =='POST':
    
        if user.is_valid():            
            try:
                user = user.save()
            except:
                print("NO PASA USER")
        else:
            print(user.non_field_errors)
            print(user.errors)
        if  user_profile.is_valid():
            try:
                user_profile = user_profile.save(commit=False)
                user_profile.user = user
                user_profile.save()
            except:
                print("NO PASA PROFILE")
        else:
            print(user_profile.non_field_errors)
            print(user_profile.errors)
    else:
        user = UserForm()
        user_profile = User_ProfileForm()
    return render(request,'register.html',{
                'user':UserForm,
                'profile':User_ProfileForm})
