# Generated by Django 4.1 on 2022-09-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca', '0007_alter_journalentry_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='task_description',
            field=models.CharField(max_length=160, null=True),
        ),
    ]