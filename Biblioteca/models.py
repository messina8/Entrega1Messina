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
