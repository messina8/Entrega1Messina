from django.contrib import admin
import login.models

# Register your models here.

admin.site.register(login.models.LogHistory)  # Shouldn't be accessible but is, for the sake of testing
admin.site.register(login.models.Profile)
