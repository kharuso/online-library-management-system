# Generated by Django 4.2.2 on 2023-08-15 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0029_borrowed_book_due_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowed_book',
            old_name='due_date',
            new_name='date_due',
        ),
        migrations.AlterField(
            model_name='borrowed_book',
            name='date_borrowed',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 14, 37, 37, 655742)),
        ),
    ]
