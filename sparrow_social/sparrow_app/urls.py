from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from django.conf.urls.static import static


urlpatterns = [
    # path('feed/',views.feed, name = "feed"),
    path('',views.home, name = "home"),
    # path('post/<str:id_post>/',views.feed, name = "postit"),
    # path('profile/', 'views.profile', name = 'profile'),
    path('profile-<int:id>/', views.profile, name = 'profile'),
    path('register/',views.register, name = "register"),
    path('login/',  LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(),name = 'logout'),
    #path('post/', views.posting, name = 'posting'),
    # path('follow/', 'views.follow', name = 'follow'),
    # path('unfollow/', 'views.unfollow', name = 'unfollow'),
    # path('followers/', 'views.followers', name = 'followers'),
    # path('following/', 'views.following', name = 'following'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
