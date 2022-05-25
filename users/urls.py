from django.urls import path, include
from django.contrib import admin
from . import views
from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('login/', views.UserLoginView, name='login'),
    path('cookie/', views.CookieView.as_view(), name='cookie'),

    path('tasks/', views.taskTables, name='tables'),
    path('taskCreate/', views.taskCreate, name='create'),

    path('game/', views.Game, name='game'),
]
