from django.contrib import admin
import chat.models

# Register your models here.
admin.site.register(chat.models.Review)  # Shouldn't be accessible but is, for the sake of testing
admin.site.register(chat.models.Message)  # Shouldn't be accessible but is, for the sake of testing
