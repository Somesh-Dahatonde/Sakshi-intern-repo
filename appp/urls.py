from unicodedata import name
from django.contrib import admin
from django.urls import path
from appp import views

urlpatterns = [

    path('', views.index, name='index'),
    path('fet', views.fet, name='fet'),
    path('index', views.home, name='index'),
    path('enter', views.enter, name='enter'),
    path('per', views.per, name='per'),
    path('thn', views.thn, 'thn'),
]
