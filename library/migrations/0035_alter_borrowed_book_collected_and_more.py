# Generated by Django 4.2.2 on 2023-08-15 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0034_alter_borrowed_book_collected_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed_book',
            name='collected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='borrowed_book',
            name='date_borrowed',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 15, 52, 33, 682983)),
        ),
        migrations.AlterField(
            model_name='borrowed_book',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]