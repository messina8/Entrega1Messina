from django.db import models


# Create your models here.
class LogHistory(models.Model):
    user_id = models.IntegerField()
    log_time = models.DateTimeField()
    log_in = models.BooleanField()
    log_out = models.BooleanField()

