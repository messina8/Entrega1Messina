from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender',
                               on_delete=models.CASCADE)  # should make a function where if both are null, delete
    message = models.TextField()
    target = models.ForeignKey(User, related_name='target',
                               on_delete=models.CASCADE)  # should make a function where if both are null, delete
    time = models.DateTimeField(auto_now=True)


class Review(models.Model):
    signature = models.CharField(max_length=80)
    review = models.TextField()
    rating = models.IntegerField()
