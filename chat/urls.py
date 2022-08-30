from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path('messages/', views.messages, name='Messages'),
    path('users/', views.user_list, name='Users'),
    path('read/', views.read_message, name='Read'),
    path('send/<user_id>', views.send_message, name='Send'),
    path('reviews/', views.reviews, name='Reviews'),
    path('new_review/', views.new_review, name='NewReview')


]
