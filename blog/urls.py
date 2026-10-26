from django.urls import path
from django.contrib import admin
from blog import views

urlpatterns = [
    path('', views.index),
]