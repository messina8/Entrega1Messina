
from django.db import models

# Create your models here.


class Message(models.Model):
    author_id = models.IntegerField()
    message = models.TextField()
    target_id = models.IntegerField()
    time = models.DateTimeField(auto_now=True)


class Review(models.Model):
    signature = models.CharField(max_length=80)
    review = models.TextField()
    rating = models.IntegerField()
