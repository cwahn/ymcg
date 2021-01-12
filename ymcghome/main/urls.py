from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('activities/', views.activities, name='activities'),
    path('join/', views.join, name='join'),
    path('elements/', views.elements, name='elements'),
]