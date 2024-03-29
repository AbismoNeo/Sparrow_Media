from asyncio.windows_events import NULL
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
import sys

###################### SUGERENCIAS DE CONTACTO ######################
def sugerencias():
    profiles = user_profile.objects.all()
    datos_salida = []
    temp = []
    for i in range(6):
        existe = False
        temporal  = (user.objects.all().order_by('?')[:1].get())
        for t in temp:
            if temporal.id == t:
                existe = True
        if existe == False:
            temp.append(temporal.id)
            for userp in profiles:
                if userp.user.id == temporal.id:
                    datos ={
                        'id':temporal.id,
                        'profilepic':userp.profilepic,
                        'watchname': userp.watchname
                        }
                    datos_salida.append(datos)
                    print(datos)
    return datos_salida

###################### NOTICIAS DE LA PLATAORMA ######################
def noticias():
    news = message.objects.filter(user_id__username ='admin')
    return news

######################  SEGUIDORES Y SEGUIDOS   ######################
def contador_seguidor(request):
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

    return (list_follow_count, list_friend_count)

######################  LISTA MENSAJES INICIO - USUARIO   ######################
def lista_mensajes_amigos(request):
    # id_list, id_friend, follow_date
    lista_amigos = list_follow.objects.filter(id_list = request.user)
    lista_mensajes = message.objects.all()
    lista_perfiles = user_profile.objects.all()
    mensajes_amigos=[]
    # datos_mensajes_amigos=[]
    for amigos in lista_amigos:
        for mensaje in lista_mensajes:
            if mensaje.user_id == amigos.id_friend:
                #postslist.append(mensaje)
                for perfil in lista_perfiles:
                    if perfil.user  == amigos.id_friend:
                #profilelist.append(perfil)
                        datos_mensajes_amigos={
                            "id" : amigos.id_friend,
                            'watchname' : perfil.watchname,
                            "profilepic" : perfil.profilepic,
                            "datepost" : mensaje.datepost,
                            "Text" : mensaje.Text,
                            }
                        mensajes_amigos.append(datos_mensajes_amigos)
    # profilelist = user_profile.objects.filter(user = lista_amigos)
    
    return ( mensajes_amigos )

def contador_profile(request,id):
    datos_contador = []
    list_follows = list_follow.objects.filter(id_friend = id )
    list_friends = list_follow.objects.filter(id_list = id )
    try:
        following = list_follow.objects.filter( id_friend = user.id, id_list = id)
        if following.count > 0:
            follow_user = True 
        else:
            follow_user = False
    except:
        follow_user = 'NO FUNCIONA'

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

    count_follow = list_follows.count()
    count_friends = list_friends.count()
    datos_contador= {
                'follow_user' : follow_user,
                'count_follow' : count_follow, 
                'count_friends' : count_friends, 
                'list_follow_count' : list_follow_count,
                'list_friend_count' : list_friend_count,
                }
    return(datos_contador)