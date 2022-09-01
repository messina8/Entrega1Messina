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
    path('new_book/', views.new_owned_book, name='NewBook'),
    path('set_read/<book_id>', views.set_book_read),
    path('to_do/', views.to_do, name='ToDo'),
    path('timetable/', views.timetable, name='Timetable'),
    path('journal/', views.journal, name='Journal'),
    path('journal_entry/<entry_id>', views.journal),
    path('new_entry/', views.new_journal_entry, name='NewEntry'),

]
