from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('', views.login, name='Login'),
    path('profile/', views.profile, name='Profile')
]
