from django.contrib import admin
from .models import Book, User, Borrowed_Book

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Borrowed_Book)
