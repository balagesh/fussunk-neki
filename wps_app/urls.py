from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.app_homepage, name='app_homepage'),
    path('matchform', views.matchform, name='matchform'),
    path('newmatch', views.newmatch, name='newmatch'),
    path('newplayer', views.newplayer, name='newplayer'),
    path('register', views.register, name="register")
]
