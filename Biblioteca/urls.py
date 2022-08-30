from django.contrib import admin
from django.urls import path
from Biblioteca import views

urlpatterns = [
    path('legacy/books/', views.books, name='Books'),
    path('legacy/clients/', views.clients, name='Clients'),
    path('legacy/invoice/', views.invoice, name='Invoice'),
    path('legacy/clientsearch/', views.client_search, name='ClientSearch'),
    path('legacy/search/', views.search),
    path('owned_books/', views.owned_books, name='OwnedBooks'),
    path('to_do/', views.to_do, name='ToDo'),
    path('timetable/', views.timetable, name='Timetable'),
    path('journal/', views.journal, name='Journal'),

]
