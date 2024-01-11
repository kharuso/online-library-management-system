from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)


    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='library/pdfs/')
    cover = models.ImageField(upload_to='library/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)  

class Borrowed_Book(models.Model):
    book = models.CharField(max_length=100)
    borrower = models.CharField(max_length=100)
    date_borrowed = models.DateTimeField(default=datetime.now())
    due_date = models.DateField(null=True)
    collected = models.BooleanField(default=False)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.book
    


        
