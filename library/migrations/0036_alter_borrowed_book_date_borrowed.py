# Generated by Django 4.1.7 on 2024-01-06 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0035_alter_borrowed_book_collected_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed_book',
            name='date_borrowed',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 6, 15, 35, 43, 468137)),
        ),
    ]
