# Generated by Django 4.2.2 on 2023-08-15 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0024_alter_borrowed_book_date_borrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed_book',
            name='date_borrowed',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 11, 44, 44, 865754)),
        ),
    ]
