# Generated by Django 4.2.2 on 2023-08-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_cover_alter_book_pdf_borrowed_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed_book',
            name='book',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='borrowed_book',
            name='borrower',
            field=models.CharField(max_length=100),
        ),
    ]
