
from django.db import models

# Create your models here.


class Message(models.Model):
    author = models.CharField(max_length=60)
    message = models.CharField(max_length=300)
    target = models.CharField(max_length=60)
    time = models.DateTimeField(auto_now=True)


# class Review(models.Model):
#     pass
