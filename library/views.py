from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import User, Book, Borrowed_Book
from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from .forms import BookForm, UserForm
from . import models
import operator
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def login_form(request):
	return render(request, 'library/login.html')


def logoutView(request):
	logout(request)
	return redirect('home')


def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return redirect('publisher')
		else:
			messages.info(request, "Invalid username or password")
			return redirect('home')


def register_form(request):
	return render(request, 'library/register.html')


def registerView(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		first_name = request.POST['fname']
		last_name = request.POST['lname']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:

			if User.objects.filter(username=username).exists():
				messages.error(request, 'Username already taken')
				return redirect('regform')

			elif User.objects.filter(email=email).exists():
				messages.error(request, 'Email already taken')
				return redirect('regform')

			else:
				password = make_password(password1)

				user = User(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
				user.save()
				messages.success(request, 'Account was created successfully')
				return redirect('home')
		else:
			messages.error(request, "Password didn't match")
			return redirect('regform')


@login_required
def uabook_form(request):
	return render(request, 'publisher/add_book.html')

@login_required
def ubbook_form(request):
	return render(request, 'publisher/borrow_book.html')


class UBookListView(ListView):
	model = Book
	template_name = 'publisher/book_list.html'
	context_object_name = 'books'
	

	def get_queryset(self):
		return Book.objects.order_by('-id')


@login_required
def uabook(request):
	if request.method == 'POST':
		title = request.POST['title']
		author = request.POST['author']
		year = request.POST['year']
		publisher = request.POST['publisher']
		desc = request.POST['desc']
		cover = request.FILES['cover']
		pdf = request.FILES['pdf']
		current_user = request.user
		user_id = current_user.id
		username = current_user.username

		a = Book(title=title, author=author, year=year, publisher=publisher, 
			desc=desc, cover=cover, pdf=pdf, uploaded_by=username, user_id=user_id)
		a.save()
		#messages.success(request, 'Book was uploaded successfully')
		return redirect('publisher')
	else:
	    #messages.error(request, 'Book was not uploaded successfully')
	    return redirect('uabook_form')	



@login_required
def ubbook(request):
	if request.method == 'POST':
		book = request.POST['title']
		due_date = request.POST['date']
		current_user = request.user
		borrower = current_user.username


		a = Borrowed_Book(book=book, borrower=borrower, due_date=due_date )
		a.save()
		#messages.success(request, 'Completed')
		return redirect('publisher')
	else:
	    #messages.error(request, 'error')
	    return redirect('ubbook_form')	



