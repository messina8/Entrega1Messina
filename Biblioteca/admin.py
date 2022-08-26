from django.contrib import admin

import Biblioteca.models


# Register your models here.
admin.site.register(Biblioteca.models.Book)
admin.site.register(Biblioteca.models.Clients)
admin.site.register(Biblioteca.models.Invoices)
admin.site.register(Biblioteca.models.ToDoItem)
admin.site.register(Biblioteca.models.TimeTable)
admin.site.register(Biblioteca.models.OwnedBooks)
admin.site.register(Biblioteca.models.JournalEntry)# Shouldn't be accessible but is,for the sake of testing
