# Generated by Django 4.2.2 on 2023-08-15 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_borrowed_book_date_borrowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed_book',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='borrowed_book',
            name='date_borrowed',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 11, 32, 26, 625395)),
        ),
    ]
