# Generated by Django 4.2.2 on 2023-08-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_remove_borrowed_book_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed_book',
            name='user_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
