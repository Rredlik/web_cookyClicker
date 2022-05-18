from django.urls import path, include
from django.contrib import admin
from . import views
from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('login/', views.LoginForm, name='login')
]
