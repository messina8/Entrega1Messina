from django.contrib import admin
from django.urls import path
from login import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name='Login'),
    path('profile/', views.profile, name='Profile'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='Logout')

]
