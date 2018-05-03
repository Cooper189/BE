from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.set_users, name='set_users'),
    path('login/', views.get_users, name='get_users'),
    path('test/', views.test, name='tests'),
]
