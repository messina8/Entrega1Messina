from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class LogHistory(models.Model):
    user_id = models.IntegerField()
    log_time = models.DateTimeField()
    log_in = models.BooleanField()
    log_out = models.BooleanField()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

