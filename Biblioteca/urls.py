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
    path('journal/', views.journal, name='Journal'),
    path('journal/edit/<entry_id>', views.edit_entry),
    path('journal_entry/<entry_id>', views.read_entry),
    path('new_entry/', views.new_journal_entry, name='NewEntry'),
    path('to_do/', views.to_do, name='ToDo'),
    path('done/', views.done, name='Done'),
    path('to_do/new_task', views.new_task, name='NewTask'),
    path('to_do/set_task_done/<task_id>', views.set_task_done),
    path('to_do/delete/<task_id>', views.delete_task, ),
    path('timetable/', views.timetable, name='Timetable'),

]
