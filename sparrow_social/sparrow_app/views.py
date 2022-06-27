from django import shortcuts
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext
from sparrow_social.settings import MEDIA_ROOT, STATIC_ROOT
from .models import user_profile, message, list_follow
from .forms import UserForm, User_ProfileForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User as user
from django.views.decorators.csrf import csrf_exempt
from .sparrow_functions import *
import sys

# Create your views here.

################# home VIEW #################
def home (request):
    if request.user.is_authenticated:
        ######### SUGERENIAS ############
        suggests= sugerencias()
        ####### AQUI SE VEN LAS NOTICIAS (POSTEOS DE ADMIN) #########
        news = noticias()
        ####### AQUI SE VE LOS SEGUIDORES Y A LOS QUE SEGUIMOS #########
        list_follow_count, list_friend_count = contador_seguidor(request)
        ####### AQUI SE VE LOS POST QUE VEREMOS #########
        datos_mensajes = lista_mensajes_amigos(request)
        

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
        context ={
            #'profilelist':profilelist, 
            'user_data': user_data, 
            'Form':form,
            'list_follow_count':list_follow_count,
            'list_friend_count':list_friend_count,
            'news':news,
            'suggests':suggests,
            'datos_mensajes' : datos_mensajes,
            }
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

def profile(request,id):
        user_visit = user.objects.get(pk=id)
        user_data_visit = user_profile.objects.get(pk=id)
        # list_follows = list_follow.objects.filter(id_friend = id )
        # list_friends = list_follow.objects.filter(id_list = id )
        postslist = message.objects.filter(user_id = id )    
        # user_me = user.objects.get(pk = request.user)
        profile_me = user_profile.objects.get( user = request.user.id)
        ############################## NEWS ###################################
        news = message.objects.filter(user_id__username ='admin')
        ########################SUGERENCIAS ###################################
        suggests=[]
        for i in range(6):
            suggests.append ((user_profile.objects.all().order_by('?')[:1].get()))
        ##################### CONTADORES PARA PERFIL ##########################
        datos_contador = contador_profile(request,id)
        
        print("######### CONT_PROFILE ##########")
        print(datos_contador)
        print("######### CONT_PROFILE ##########")

        context ={  
                    'user_visit':user_visit,
                    'user_data_visit':user_data_visit,
                    'count_follow':datos_contador.count_follow,
                    'count_friends' : datos_contador.count_friends,
                    'follow_user' : datos_contador.follow_user,
                    'postslist' : postslist,
                    'user_data' : profile_me,
                    'news':news,
                    'suggests':suggests,
                    'list_follow_count' : datos_contador.list_follow_count,
                    'list_friend_count' : datos_contador.list_friend_count
                    }
        return render(request, 'profile_user.html', context)

def followers(request, id ):
    lista_seguidores = []
    user_visit={'id': id}
    titulo ='Followers'
    suggests= sugerencias()
    count_follow, count_friends = contador_profile(request,id)
    news = message.objects.filter(user_id__username ='admin')
    user_data = user_profile.objects.get( user = request.user.id)
    user_data_visit = user_profile.objects.get(user= id)
    list_follow_count, list_friend_count = contador_seguidor(request)
    # if request.user.id == id :
    #     lista = list_follow.objects.filter(id_friend = request.user.id )
    # else:
    lista = list_follow.objects.filter(id_friend = id )
    for dato in lista:
        perfil = user_profile.objects.get(user = dato.id_list)
        dato_guarda ={
                    'id': dato.id_list,
                    'user_visit.id':id,
                    'watchname': perfil.watchname,
                    'description': perfil.description,
                    'profilepic' : perfil.profilepic,
                    }
        lista_seguidores.append(dato_guarda)
    context = {
            'id': id,
            'lista_datos' : lista_seguidores,
            'titulo' : titulo,
            'user_visit': user_visit,
            'suggests': suggests,
            'list_follow_count' : list_follow_count,
            'list_friend_count' : list_friend_count,
            'user_data':user_data,
            'user_data_visit':user_data_visit,
            'news': news,
            'count_follow':count_follow.count_follow,
            'count_friends':count_friends.count_friends,
            }
    return render(request, 'follows_list.html', context)


def following(request, id ):
    lista_seguidores = []
    titulo  = "Following"
    suggests= sugerencias()
    news = message.objects.filter(user_id__username ='admin')
    list_follow_count, list_friend_count = contador_seguidor(request)
    user_visit={'id': id}
    cont_prof = contador_profile(request,id)
        
    user_data_visit = user_profile.objects.get(user= id)
    user_data = user_profile.objects.get( user = request.user.id)
    # if request.user.id == id :
    #     lista = list_follow.objects.filter(id_list = request.user.id )
    # else:
    lista = list_follow.objects.filter(id_list = id )
    for dato in lista:
        perfil = user_profile.objects.get(user = dato.id_friend)
        dato_guarda ={
                    'id': dato.id_friend,
                    'user_data': perfil.watchname,
                    'description': perfil.description,
                    'profilepic' : perfil.profilepic,
                    }
        lista_seguidores.append(dato_guarda)
    context = {
            'id':id,
            'lista_datos' : lista_seguidores,
            'titulo' : titulo,
            'user_visit': user_visit,
            'suggests': suggests,
            'list_follow_count' : list_follow_count,
            'list_friend_count' : list_friend_count,
            'user_data':user_data,
            'user_data_visit':user_data_visit,
            'news': news,
            'count_follow':cont_prof["count_follow"],
            'count_friends':cont_prof["count_friends"],
            }
    return render(request, 'follows_list.html', context)