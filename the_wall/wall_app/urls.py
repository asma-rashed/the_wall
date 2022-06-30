from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login',views.login),
    path('logout',views.logout),
    path('wall',views.wall),
    path('msg',views.msg),
    path('comment',views.comment)
]