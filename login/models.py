from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class LogHistory(models.Model):
    user_id = models.IntegerField()
    log_time = models.DateTimeField(auto_now=True)
    log_in = models.BooleanField(default=False)
    log_out = models.BooleanField(default=False)  # wanted to add to "logout" view, but passed it from urls.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

