# Generated by Django 4.2.2 on 2023-06-30 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='book',
            name='lname',
        ),
    ]
