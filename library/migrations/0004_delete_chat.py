# Generated by Django 4.2.2 on 2023-07-04 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_user_is_librarian_chat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
