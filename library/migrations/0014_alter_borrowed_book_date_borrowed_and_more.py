# Generated by Django 4.2.2 on 2023-08-15 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_borrowed_book_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed_book',
            name='date_borrowed',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 11, 34, 48, 491915)),
        ),
        migrations.AlterField(
            model_name='borrowed_book',
            name='returned',
            field=models.SlugField(null=True),
        ),
    ]
