# Generated by Django 4.2.2 on 2023-08-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_remove_borrowed_book_date_borrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed_book',
            name='due_date',
            field=models.DateField(null=True),
        ),
    ]
