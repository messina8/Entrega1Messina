# Generated by Django 4.1 on 2022-08-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='invoice_number',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
