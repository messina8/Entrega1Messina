
from django.urls import path
from login import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name='Login'),
    path('profile/', views.profile, name='Profile'),
    path('edit_profile/', views.edit_profile, name='EditProfile'),
    path('change_password', views.change_password, name='ChangePassword'),
    path('logout/', LogoutView.as_view(template_name='login/logout.html'), name='Logout'),
    path('sign_in/', views.register, name='Register'),

]
