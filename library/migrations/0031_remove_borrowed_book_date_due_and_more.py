# Generated by Django 4.2.2 on 2023-08-15 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0030_rename_due_date_borrowed_book_date_due_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowed_book',
            name='date_due',
        ),
        migrations.AlterField(
            model_name='borrowed_book',
            name='date_borrowed',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 14, 39, 48, 848544)),
        ),
    ]