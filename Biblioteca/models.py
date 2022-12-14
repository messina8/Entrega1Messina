from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=15)
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    theme = models.CharField(max_length=20)


class Invoices(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=True)
    client_name = models.CharField(max_length=40)
    book_id = models.IntegerField()
    total = models.IntegerField()


class Clients(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    id_number = models.IntegerField()
    address = models.CharField(max_length=60)


class OwnedBooks(models.Model):
    isbn = models.CharField(max_length=15)
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    theme = models.CharField(max_length=20)
    read = models.BooleanField(default=False)
    read_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.author}'


class ToDoItem(models.Model):
    done = models.BooleanField(default=False)
    time_when_done = models.DateTimeField(null=True)
    task = models.CharField(max_length=40)
    task_description = models.CharField(max_length=160, null=True)
    expiration_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.task}'


class TimeTable(models.Model):
    time = models.TimeField()
    activity = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.activity}'

    class Meta:
        unique_together = (("user", "time"),)
        ordering = ['time']


class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    entry = models.TextField()

    class Meta:
        unique_together = (("user", "date"),)
        ordering = ['-date']

    def __str__(self):
        return f'{self.user} {self.date} entry'
