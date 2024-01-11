from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.login_form, name='home'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('regform/', views.register_form, name='regform'),
    path('register/', views.registerView, name='register'),

    path('publisher/', views.UBookListView.as_view(), name='publisher'),
    path('uabook_form/', views.uabook_form, name='uabook_form'),
    path('uabook/', views.uabook, name='uabook'),
    path('ubbook_form/', views.ubbook_form, name='ubbook_form'),
    path('ubbook/', views.ubbook, name='ubbook'),
   
]